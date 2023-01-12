# -*- coding: utf-8 -*-

from odoo import models, fields, api
# class customizations(models.Model):
#     _name = 'customizations.customizations'
#     _description = 'customizations.customizations'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100



#M

class Penalties(models.Model):
    _name = "customizations.penalties"
    _description = "New Form"

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, readonly=True, help="Employee",

                                  states={'draft': [('readonly', False)]})
    @api.depends('value')
    def _value_pc(self):
            for record in self:
                record.value2 = float(record.value) / 100
