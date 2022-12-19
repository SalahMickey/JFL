from odoo import api, fields, models, _
from odoo.exceptions import UserError


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    # analytic_id = fields.Many2one("account.analytic.account", string="Analytic Accounts", required=False)
    analytic_tag_id = fields.Many2one("account.analytic.tag", string="Analytic Tags", required=True,
                                      related='employee_id.analytic_tag_id')
    cost_center_id = fields.Many2one("cost.center", string="Cost Center", required=True,
                                     related='employee_id.cost_center_id')

    def action_payslip_done(self):
        res = super(HrPayslip, self).action_payslip_done()

        for slip in self:
            line_ids = []
            analytic_tags = []
            debit_sum = 0.0
            credit_sum = 0.0
            date = slip.date or slip.date_to
            currency = slip.company_id.currency_id
            analytic_tags.append(slip.analytic_tag_id.id)
            name = _('Payslip of %s') % (slip.employee_id.name)
            print("/////////////cost_center_id", slip.cost_center_id)
            print("/////////////analytic_tags", analytic_tags)
            move_dict = {
                'narration': name,
                'ref': slip.number,
                'journal_id': slip.journal_id.id,
                'cost_center_id': slip.cost_center_id.id,
                'date': date,
            }
            for line in slip.details_by_salary_rule_category:
                amount = currency.round(slip.credit_note and -line.total or line.total)
                if currency.is_zero(amount):
                    continue
                debit_account_id = line.salary_rule_id.account_debit.id
                credit_account_id = line.salary_rule_id.account_credit.id

                if debit_account_id:
                    debit_line = (0, 0, {
                        'name': line.name,
                        'partner_id': line._get_partner_id(credit_account=False),
                        'account_id': debit_account_id,
                        'journal_id': slip.journal_id.id,
                        'cost_center_id': slip.cost_center_id.id,
                        'date': date,
                        'debit': amount > 0.0 and amount or 0.0,
                        'credit': amount < 0.0 and -amount or 0.0,
                        'analytic_account_id': line.salary_rule_id.analytic_account_id.id,
                        'analytic_tag_ids': [(6, 0, analytic_tags)],
                        'tax_line_id': line.salary_rule_id.account_tax_id.id,
                    })
                    line_ids.append(debit_line)
                    debit_sum += debit_line[2]['debit'] - debit_line[2]['credit']
                if credit_account_id:
                    credit_line = (0, 0, {
                        'name': line.name,
                        'partner_id': line._get_partner_id(credit_account=True),
                        'account_id': credit_account_id,
                        'journal_id': slip.journal_id.id,
                        'cost_center_id': slip.cost_center_id.id,
                        'date': date,
                        'debit': amount < 0.0 and -amount or 0.0,
                        'credit': amount > 0.0 and amount or 0.0,
                        'analytic_account_id': line.salary_rule_id.analytic_account_id.id,
                        'analytic_tag_ids': [(6, 0, analytic_tags)],
                        'tax_line_id': line.salary_rule_id.account_tax_id.id,
                    })
                    line_ids.append(credit_line)
                    credit_sum += credit_line[2]['credit'] - credit_line[2]['debit']

            if currency.compare_amounts(credit_sum, debit_sum) == -1:
                acc_id = slip.journal_id.default_credit_account_id.id
                if not acc_id:
                    raise UserError(_('The Expense Journal "%s" has not properly configured the Credit Account!') % (
                        slip.journal_id.name))
                adjust_credit = (0, 0, {
                    'name': _('Adjustment Entry'),
                    'partner_id': False,
                    'account_id': acc_id,
                    'journal_id': slip.journal_id.id,
                    'analytic_tag_ids': [(6, 0, analytic_tags)],
                    'date': date,
                    'debit': 0.0,
                    'credit': currency.round(debit_sum - credit_sum),
                })
                line_ids.append(adjust_credit)

            elif currency.compare_amounts(debit_sum, credit_sum) == -1:
                acc_id = slip.journal_id.default_debit_account_id.id
                if not acc_id:
                    raise UserError(_('The Expense Journal "%s" has not properly configured the Debit Account!') % (
                        slip.journal_id.name))
                adjust_debit = (0, 0, {
                    'name': _('Adjustment Entry'),
                    'partner_id': False,
                    'account_id': acc_id,
                    'journal_id': slip.journal_id.id,
                    'analytic_tag_ids': [(6, 0, analytic_tags)],
                    'date': date,
                    'debit': currency.round(credit_sum - debit_sum),
                    'credit': 0.0,
                })
                line_ids.append(adjust_debit)
            move_dict['line_ids'] = line_ids
            move = self.env['account.move'].create(move_dict)
            slip.write({'move_id': move.id, 'date': date})
            print(move)
            print(move.line_ids)
            if not move.line_ids:
                raise UserError(_("As you installed the payroll accounting module you have to choose Debit and Credit"
                                  " account for at least one salary rule in the choosen Salary Structure."))
            move.post()
        return res

    # def action_payslip_done(self):
    #     """
    #     function used for marking paid Attendance/Leave request.
    #     """
    #     for rec in self:
    #         rec.payslip_paid = True
    #     return super(HrPayslip, self).action_payslip_done()
