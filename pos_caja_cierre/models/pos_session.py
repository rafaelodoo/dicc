from odoo import models, fields, api

class PosSession(models.Model):
    _inherit = 'pos.session'

    # Aquí irán los campos adicionales que necesitemos 

class PosConfig(models.Model):
    _inherit = 'pos.config'

    hide_cash_details_on_closing = fields.Boolean(
        'Ocultar Detalles de Efectivo en Cierre',
        help='Si está marcado, los detalles de apertura, pagos y diferencia de efectivo se ocultarán en el popup de cierre de caja.',
        default=False
    ) 