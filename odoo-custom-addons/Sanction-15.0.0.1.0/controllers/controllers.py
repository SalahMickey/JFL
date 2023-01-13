from odoo import http


class Sanction(http.Controller):
      @http.route('/sanction', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('sanction/objects', auth='public')
       def list(self, **kw):
         return http.request.render('sanction listing', {
             'root': '/sanction',
             'objects': http.request.env['sanction'].search([]),
         }

     @http.route('sanction/objects/<model("sanction"):obj>', auth='public')
     def object(self, obj, **kw):
         return http.request.render('sanction.object', {
             'object': obj
         })
