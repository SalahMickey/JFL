# -*- coding: utf-8 -*-
# from odoo import http


# class HrPayrollCostCenter(http.Controller):
#     @http.route('/hr_payroll_cost_center/hr_payroll_cost_center/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_payroll_cost_center/hr_payroll_cost_center/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_payroll_cost_center.listing', {
#             'root': '/hr_payroll_cost_center/hr_payroll_cost_center',
#             'objects': http.request.env['hr_payroll_cost_center.hr_payroll_cost_center'].search([]),
#         })

#     @http.route('/hr_payroll_cost_center/hr_payroll_cost_center/objects/<model("hr_payroll_cost_center.hr_payroll_cost_center"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_payroll_cost_center.object', {
#             'object': obj
#         })
