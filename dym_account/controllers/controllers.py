# -*- coding: utf-8 -*-
# from odoo import http


# class DymAccount(http.Controller):
#     @http.route('/dym_account/dym_account', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dym_account/dym_account/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dym_account.listing', {
#             'root': '/dym_account/dym_account',
#             'objects': http.request.env['dym_account.dym_account'].search([]),
#         })

#     @http.route('/dym_account/dym_account/objects/<model("dym_account.dym_account"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dym_account.object', {
#             'object': obj
#         })
