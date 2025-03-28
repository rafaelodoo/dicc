{
    'name': 'Agregar Búsqueda en Autopedido',
    'version': '1.0',
    'summary': 'Agrega funcionalidad de búsqueda por nombre y referencia en el módulo de autopedido.',
    'description': """
        Este módulo agrega una vista de búsqueda a la vista de productos en el módulo de autopedido,
        permitiendo a los usuarios buscar productos por nombre y referencia.
    """,
    'author': 'Tu Nombre',
    'category': 'Point of Sale',
    'depends': ['pos_self_order'],  # Dependencia del módulo pos_self_order
    'data': [
        'views/product_template.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}