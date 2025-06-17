{
    'name': 'POS Self Order Search',
    'version': '1.0',
    'category': 'Point of Sale',
    'summary': 'Add search functionality to POS Self Order',
    'description': """
        This module adds a search bar to the POS Self Order interface,
        allowing customers to search for products dynamically.
    """,
    'author': 'DICC - Desarrollo e Innovación',
    'website': 'https://github.com/tu-org/dicc',
    'license': 'LGPL-3',
    'depends': [
        'point_of_sale',
        'pos_self_order',
    ],
    'data': [
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_backend': [
            'pos_self_order_search/static/src/overrides/SelfOrderScreen.js',
            'pos_self_order_search/static/src/overrides/SelfOrderScreen.xml',
            'pos_self_order_search/static/src/overrides/SelfOrderScreen.scss',
        ],
    },
    'demo': [],
    'test': [
        'tests/test_pos_session_search.py',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
} 