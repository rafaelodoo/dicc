# -*- coding: utf-8 -*-
{
    'name': 'POS Self-Order Product Search (V18)', # Nombre claro
    'version': '18.0.1.0.0',
    'category': 'Sales/Point of Sale',
    'summary': 'Adds product search functionality to the POS Self-Order screen (V18).',
    'description': """
This module adds a search bar to the product list page of the Odoo 18
Point of Sale Self-Order interface.
    """,
    'author': 'Tu Nombre/Empresa Aquí', # Puedes poner tu autoría
    'website': 'https://www.tuwebsite.com', # Opcional
    'depends': [
        'pos_self_order', # Dependencia clave del módulo base v18
    ],
    'assets': {
        # Bundle de assets del autopedido donde inyectaremos nuestro JS
        'pos_self_order.assets_self_order': [
            # Ruta relativa desde la raíz de addons
            'pos_self_order_search_v18/static/src/app/pages/product_list_page/product_list_page.js',
        ],
        # Bundle de assets QWeb donde inyectaremos nuestra plantilla XML modificada
        'web.assets_qweb': [
             'pos_self_order_search_v18/views/pos_self_order_product_list_page_view.xml',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}