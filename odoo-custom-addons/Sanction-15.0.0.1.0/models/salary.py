from odoo import models, fields


class SanctionRule(models.Model):

    _inherit = 'hr.salary.rule'

    sanction_id = fields.Many2one("sanction", string="Sanction")