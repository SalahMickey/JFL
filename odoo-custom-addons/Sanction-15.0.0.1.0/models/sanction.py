from odoo import models, fields, api


class Sanction(models.Model):
    _name = 'sanction'
    _description = 'employee sanction'

    name = fields.Char("title")
    code = fields.Char("Code")
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)

    @api.model
    @api.depends('code', 'name')
    def name_search(self, name, args=None, operator='like', limit=100):
        args = args or []
        domain = []
        result = []

        if name:
            domain = ['|', ('name', operator, name), ('code', operator, name)]
        csm = self.search(domain + args, limit=limit)

        for cost_center in csm:
            name = Sanction.code + ' ' + Sanction.name
            result.append((Sanction.id, name))
        return result
