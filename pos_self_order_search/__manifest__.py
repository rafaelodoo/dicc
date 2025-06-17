{
    'name': 'POS Self Order - Product Search',
    'version': '18.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Endpoint RPC para búsqueda de productos en Autopedido',
    'description': """
        Extensión para el módulo pos_self_order que proporciona un endpoint RPC
        para la búsqueda eficiente de productos desde la interfaz de autopedido.
        
        Características:
        - Búsqueda por nombre y código interno de producto
        - Filtrado por productos disponibles en PdV
        - Búsqueda insensible a mayúsculas y minúsculas
        - Retorno optimizado de datos esenciales del producto
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
    'assets': {},
    'demo': [],
    'test': [
        'tests/test_pos_session_search.py',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
} 