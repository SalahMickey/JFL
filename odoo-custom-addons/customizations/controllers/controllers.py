# -*- coding: utf-8 -*-
# from odoo import http


# class Customizations(http.Controller):
#     @http.route('/customizations/customizations', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customizations/customizations/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('customizations.listing', {
#             'root': '/customizations/customizations',
#             'objects': http.request.env['customizations.customizations'].search([]),
#         })

#     @http.route('/customizations/customizations/objects/<model("customizations.customizations"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customizations.object', {
#             'object': obj
#         })
