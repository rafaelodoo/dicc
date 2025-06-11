from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    hide_cash_details_on_closing = fields.Boolean(
        string='Ocultar detalles de efectivo al cerrar',
        help='Si está marcado, se ocultarán los detalles de efectivo al cerrar la caja',
        config_parameter='pos_caja_cierre.hide_cash_details_on_closing'
    ) 