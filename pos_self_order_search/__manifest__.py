# -*- coding: utf-8 -*-
{
    'name': 'POS Self-Order Product Search',
    'version': '18.0.1.0.0',
    'category': 'Sales/Point of Sale',
    'summary': 'Adds product search functionality to the POS Self-Order screen.',
    'description': """
This module reintroduces the product search bar in the Odoo 18 Point of Sale
Self-Order interface, similar to the functionality present in Odoo 17.
    """,
    'depends': [
        'pos_self_order', # Dependencia fundamental
    ],
    'assets': {
        # Especificamos el bundle de assets del autopedido para añadir nuestros JS
        'pos_self_order.assets_self_order': [
            # Asegúrate de que la ruta sea correcta desde la raíz del servidor
            'pos_self_order_search/static/src/app/pages/product_list_page/product_list_page.js',
        ],
        # Añadimos nuestro XML de vista/template heredado
        'web.assets_qweb': [
             'pos_self_order_search/views/pos_self_order_product_list_page.xml',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False, # Opcional: True si quieres que se instale automáticamente cuando pos_self_order se instale
    'license': 'LGPL-3', # O el tipo de licencia que prefieras
}