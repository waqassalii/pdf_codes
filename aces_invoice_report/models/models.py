# -*- coding: utf-8 -*-

# from odoo import models, fields, api
#
#
# class PdfReportRadical(models.AbstractModel):
#     _name = 'report.module_name.report_template_name'
#     _description = 'Printing Report By Parser Function'
#
#     @api.model
#     def _get_report_values(self, docids, data=None):
#         docs = self.env['radical.academy'].search[()]
#         return{
#             'docs': docs,
#             'email': 'waqas@gmail.com'
#         }


# class prince_art(models.Model):
#     _name = 'prince_art.prince_art'
#     _description = 'prince_art.prince_art'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
