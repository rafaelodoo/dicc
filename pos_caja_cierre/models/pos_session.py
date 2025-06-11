from odoo import models, fields, api

class PosSession(models.Model):
    _inherit = 'pos.session'

    # Aquí irán los campos adicionales que necesitemos 