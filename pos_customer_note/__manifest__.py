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
    'assets': {
        'point_of_sale.assets': [
            'pos_customer_note/static/src/app/**/*',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}