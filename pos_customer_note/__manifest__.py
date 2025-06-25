{
    'name': 'TPV Nota del Cliente',
    'version': '18.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Añade un botón para ver las notas del cliente en el TPV.',
    'description': """
        Este módulo es un ejercicio práctico que añade un botón en la interfaz
        del Punto de Venta para mostrar las notas internas del cliente seleccionado.
    """,
    'author': 'rafael López Flores',
    'website': 'https://www.dicc.com.mx',
    'depends': [
        'point_of_sale', # Nuestra dependencia fundamental
    ],
    'data': [
        'views/pos_views.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_customer_note/static/src/app/components/customer_note_button/customer_note_button.xml',
            'pos_customer_note/static/src/app/components/customer_note_button/customer_note_button.js',
            'pos_customer_note/static/src/app/components/customer_note_button/customer_note_button.scss',
            'pos_customer_note/static/src/app/screens/product_screen/product_screen.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}