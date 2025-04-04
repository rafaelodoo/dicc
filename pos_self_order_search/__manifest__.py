{
    'name': 'POS Self Order Search',
    'version': '1.0',
    'category': 'Sales/Point of Sale',
    'sequence': 20,
    'summary': 'Add search functionality to POS Self Order',
    'description': """
This module adds search functionality to the POS Self Order interface,
allowing customers to search for products in both mobile and desktop views.
    """,
    'depends': ['pos_self_order'],
    'data': [],
    'assets': {
        'pos_self_order.assets': [
            'pos_self_order_search/static/src/app/pages/product_list_page/**/*',
        ],
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
} 