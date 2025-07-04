# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class practica_real_state(models.Model):
#     _name = 'practica_real_state.practica_real_state'
#     _description = 'practica_real_state.practica_real_state'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100