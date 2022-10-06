# -*- coding: utf-8 -*-
# from odoo import http


# class PrinceArt(http.Controller):
#     @http.route('/prince_art/prince_art/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prince_art/prince_art/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('prince_art.listing', {
#             'root': '/prince_art/prince_art',
#             'objects': http.request.env['prince_art.prince_art'].search([]),
#         })

#     @http.route('/prince_art/prince_art/objects/<model("prince_art.prince_art"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prince_art.object', {
#             'object': obj
#         })
