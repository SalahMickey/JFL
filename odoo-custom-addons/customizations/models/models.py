# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Model
class hrEmployeeInherit(models.Model):
    _inherit = "res.users" # Inherited Model

    additional_note = fields.Char(string='Additional Note')

