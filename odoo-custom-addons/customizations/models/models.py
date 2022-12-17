# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Model
class hrEmployeeInherit(models.Model):
    _inherit = "hr.employees" # Inherited Model

    bank_code = fields.Char(string='Bank Code')
    bank_acc_num = fields.Char(string='Bank Account')
