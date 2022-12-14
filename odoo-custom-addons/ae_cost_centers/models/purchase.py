# -*- coding: utf-8 -*-
##############################################################################
#    Copyright (C) 2020 AtharvERP (<http://atharverp.com/>). All Rights Reserved
# Odoo Proprietary License v1.0
#
# This software and associated files (the "Software") may only be used (executed,
# modified, executed after modifications) if you have purchased a valid license
# from the authors, typically via Odoo Apps, atharverp.com or you have written agreement from
# author of this software owner.
#
# You may develop Odoo modules that use the Software as a library (typically
# by depending on it, importing it and using its resources), but without copying
# any source code or material from the Software. You may distribute those
# modules under the license of your choice, provided that this license is
# compatible with the terms of the Odoo Proprietary License (For example:
# LGPL, MIT, or proprietary licenses similar to this one).
#
# It is forbidden to publish, distribute, sublicense, or sell copies of the Software
# or modified copies of the Software.
#
# The above copyright notice and this permission notice must be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
##############################################################################

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    cost_center_id = fields.Many2one("cost.center", string="Cost Center", store=True)

    @api.onchange('cost_center_id')
    def set_cost_center(self):
        for line in self.order_line:
            line.cost_center_id = self.cost_center_id.id

    def _prepare_invoice(self):
        """
        Prepare the dict of values to create the new invoice for a sales order. This method may be
        overridden to implement custom invoice generation (making sure to call super() to establish
        a clean extension chain).
        """
        self.ensure_one()
        result = super(PurchaseOrder, self)._prepare_invoice()
        result.update({
            'cost_center_id': self.cost_center_id and self.cost_center_id.id or False
        })
        return result


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    cost_center_id = fields.Many2one("cost.center", string="Cost Center", store=True)

    def _prepare_account_move_line(self, move=False):
        self.ensure_one()
        result = super(PurchaseOrderLine, self)._prepare_account_move_line()
        result.update({
            'cost_center_id': self.cost_center_id and self.cost_center_id.id or False
        })
        return result

    # @api.onchange('product_qty')
    # def set_default_cost_center(self):
    #     if self.order_id.cost_center_id:
    #         self.cost_center_id = self.order_id.cost_center_id.id
