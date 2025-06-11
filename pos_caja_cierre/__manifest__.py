{
    'name': 'POS Caja Cierre',
    'version': '1.0',
    'category': 'Sales/Point of Sale',
    'sequence': 20,
    'summary': 'Funcionalidad de cierre de caja para POS',
    'description': """
Este módulo agrega funcionalidades específicas para el cierre de caja en el POS.
    """,
    'depends': ['point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/pos_views.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_caja_cierre/static/src/js/**/*',
            'pos_caja_cierre/static/src/xml/**/*',
            'pos_caja_cierre/static/src/scss/**/*',
        ],
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
} 