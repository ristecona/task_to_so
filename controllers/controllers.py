# -*- coding: utf-8 -*-
from odoo import http

# class NebizTaskToSo(http.Controller):
#     @http.route('/nebiz_task_to_so/nebiz_task_to_so/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nebiz_task_to_so/nebiz_task_to_so/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nebiz_task_to_so.listing', {
#             'root': '/nebiz_task_to_so/nebiz_task_to_so',
#             'objects': http.request.env['nebiz_task_to_so.nebiz_task_to_so'].search([]),
#         })

#     @http.route('/nebiz_task_to_so/nebiz_task_to_so/objects/<model("nebiz_task_to_so.nebiz_task_to_so"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nebiz_task_to_so.object', {
#             'object': obj
#         })