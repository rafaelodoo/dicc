# -*- coding: utf-8 -*-
# from odoo import http


# class PracticaRealState(http.Controller):
#     @http.route('/practica_real_state/practica_real_state', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/practica_real_state/practica_real_state/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('practica_real_state.listing', {
#             'root': '/practica_real_state/practica_real_state',
#             'objects': http.request.env['practica_real_state.practica_real_state'].search([]),
#         })

#     @http.route('/practica_real_state/practica_real_state/objects/<model("practica_real_state.practica_real_state"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('practica_real_state.object', {
#             'object': obj
#         })
