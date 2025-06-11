from odoo import fields, models

class PosConfig(models.Model):
    _inherit = 'pos.config'

    hide_cash_details_on_closing = fields.Boolean(
        string='Ocultar detalles de efectivo al cerrar',
        help='Si está marcado, se ocultarán los detalles de efectivo al cerrar la caja'
    ) 