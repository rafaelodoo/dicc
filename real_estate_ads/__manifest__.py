{
    'name': 'Real Estate Ads',
    'version': '1.0',
    'category': 'Personalizado',
    'summary': 'Permite agregar una nota del cliente en el ticket del TPV',
    'description': """
Este módulo permite que el cajero agregue una nota personalizada del cliente en el ticket del TPV.
    """,
    'author': 'rafael López Flores',
    'depends': ['point_of_sale'],
    'data': [
        # Aquí puedes agregar otras vistas o archivos de datos si los tienes
    ],
    'assets': {
        'point_of_sale.assets_prod': [
            'pos_customer_note/static/src/app/components/customer_note_button/customer_note_button.xml',
            'pos_customer_note/static/src/app/components/customer_note_button/customer_note_button.js',
            'pos_customer_note/static/src/app/components/customer_note_button/customer_note_button.scss',
            'pos_customer_note/static/src/app/components/customer_note_button/control_buttons_extend.xml',
            'pos_customer_note/static/src/app/screens/product_screen/product_screen.js',
        ],
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}