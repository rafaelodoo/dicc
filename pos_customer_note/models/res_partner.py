# -*- coding: utf-8 -*-
from odoo import models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _get_pos_ui_res_partner(self, params): 
        """
        Heredamos este método para añadir el campo 'comment' a los datos
        del cliente que se cargan en la interfaz del TPV.

        VALIDACIÓN DE RUTA: El método original se encuentra en
        odoo/addons/point_of_sale/models/res_partner.py
        """
        # Llamamos al método original para no perder los campos base
        fields_to_load = super()._get_pos_ui_res_partner(params)

        # Añadimos nuestro campo a la lista si aún no está presente
        if 'comment' not in fields_to_load:
            fields_to_load.append('comment')

        return fields_to_load