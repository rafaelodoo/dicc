# -*- coding: utf-8 -*-

import logging
from odoo import api, models, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class PosSession(models.Model):
    _inherit = 'pos.session'

    @api.model
    def search_products_for_self_order(self, query):
        """
        Método RPC para búsqueda de productos en Autopedido.
        
        Busca productos que coincidan con la query en nombre o código interno,
        filtrando solo aquellos disponibles para el Punto de Venta.
        
        Args:
            query (str): Cadena de texto para buscar en name y default_code
            
        Returns:
            list: Lista de diccionarios con datos esenciales del producto
                  o lista vacía si no hay coincidencias
        """
        try:
            # Validar entrada
            if not query or not isinstance(query, str):
                _logger.warning('Query inválida recibida: %s', query)
                return []
            
            # Limpiar query de espacios extra
            query = query.strip()
            if not query:
                return []
            
            _logger.info('Buscando productos con query: "%s"', query)
            
            # Construir dominio de búsqueda
            domain = [
                '|',  # Operador OR
                ('default_code', 'ilike', query),
                ('name', 'ilike', query),
                ('available_in_pos', '=', True),  # Solo productos disponibles en PdV
            ]
            
            # Buscar productos
            products = self.env['product.product'].search(domain, limit=50)
            
            if not products:
                _logger.info('No se encontraron productos para la query: "%s"', query)
                return []
            
            # Preparar datos de retorno
            result = []
            for product in products:
                try:
                    product_data = {
                        'id': product.id,
                        'display_name': product.display_name,
                        'name': product.name,
                        'default_code': product.default_code or '',
                        'lst_price': product.lst_price,
                        'standard_price': product.standard_price,
                        'uom_id': [product.uom_id.id, product.uom_id.name] if product.uom_id else False,
                        'categ_id': [product.categ_id.id, product.categ_id.name] if product.categ_id else False,
                        'available_in_pos': product.available_in_pos,
                        'sale_ok': product.sale_ok,
                        'active': product.active,
                    }
                    
                    # Agregar imagen si existe
                    if product.image_128:
                        product_data['image_128'] = product.image_128
                    
                    # Agregar taxes si existen
                    if product.taxes_id:
                        product_data['taxes_id'] = [[6, 0, product.taxes_id.ids]]
                    
                    result.append(product_data)
                    
                except Exception as e:
                    _logger.error('Error procesando producto %s: %s', product.id, str(e))
                    continue
            
            _logger.info('Encontrados %d productos para la query: "%s"', len(result), query)
            return result
            
        except Exception as e:
            _logger.error('Error en search_products_for_self_order: %s', str(e))
            raise UserError(_('Error al buscar productos: %s') % str(e)) 