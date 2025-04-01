# -*- coding: utf-8 -*-
{
    'name': 'POS Self Order Button',
    'version': '1.0',
    'summary': 'Añade un botón personalizado a la pantalla de inicio del POS Self Order',
    'depends': ['pos_self_order'],
    'assets': {
        'pos_self_order.assets': [
            'pos_self_order_button/static/src/js/landing_page_extend.js',
            'pos_self_order_button/static/src/xml/landing_page_extend.xml',
        ],
    },
    'license': 'LGPL-3',
}