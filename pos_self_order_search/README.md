# POS Self Order - Product Search

## Descripción

Módulo que extiende la funcionalidad del POS Self Order agregando un endpoint RPC para la búsqueda eficiente de productos desde la interfaz de autopedido.

## Funcionalidades

- **Búsqueda por nombre y código interno**: Permite buscar productos tanto por su nombre como por su código interno (default_code)
- **Filtrado por disponibilidad**: Solo retorna productos que están disponibles en el Punto de Venta (`available_in_pos = True`)
- **Búsqueda insensible a mayúsculas**: Utiliza el operador `ilike` para búsquedas que no distingan entre mayúsculas y minúsculas
- **Retorno optimizado**: Devuelve solo los datos esenciales del producto necesarios para la interfaz

## Implementación Técnica

### Método RPC

El módulo extiende el modelo `pos.session` con el método `search_products_for_self_order`:

```python
@api.model
def search_products_for_self_order(self, query):
    """
    Busca productos que coincidan con la query en nombre o código interno.
    
    Args:
        query (str): Cadena de texto para buscar
        
    Returns:
        list: Lista de diccionarios con datos del producto
    """
```

### Dominio de búsqueda

```python
domain = [
    '|',  # Operador OR
    ('default_code', 'ilike', query),
    ('name', 'ilike', query),
    ('available_in_pos', '=', True),
]
```

### Campos retornados

- `id`: ID del producto
- `display_name`: Nombre para mostrar
- `name`: Nombre del producto
- `default_code`: Código interno
- `lst_price`: Precio de venta
- `standard_price`: Costo estándar
- `uom_id`: Unidad de medida
- `categ_id`: Categoría del producto
- `available_in_pos`: Disponible en PdV
- `sale_ok`: Puede venderse
- `active`: Activo
- `image_128`: Imagen del producto (si existe)
- `taxes_id`: Impuestos aplicables

## Instalación

1. Asegurar que los módulos `point_of_sale` y `pos_self_order` estén instalados
2. Instalar este módulo desde la interfaz de aplicaciones de Odoo
3. El endpoint estará disponible inmediatamente

## Uso desde JavaScript

```javascript
// Ejemplo de llamada RPC desde el frontend
this.rpc({
    model: 'pos.session',
    method: 'search_products_for_self_order',
    args: ['texto_busqueda'],
}).then(function(products) {
    console.log('Productos encontrados:', products);
});
```

## Criterios de Aceptación

- ✅ El endpoint RPC está creado y es accesible desde el `pos.session`
- ✅ Al pasarle una `query` válida, retorna una lista de productos que coinciden por `name` o `default_code`
- ✅ Al pasarle una `query` sin coincidencias, retorna una lista vacía `[]`
- ✅ La búsqueda filtra correctamente y solo devuelve productos con `available_in_pos = True`

## Logging y Debug

El módulo incluye logging detallado para facilitar el debug:
- Información sobre queries recibidas
- Número de productos encontrados
- Errores en el procesamiento de productos individuales
- Warnings para queries inválidas

## Dependencias

- `point_of_sale`: Módulo base del Punto de Venta
- `pos_self_order`: Módulo de Autopedido de Odoo

## Versión

- **Versión**: 18.0.1.0.0
- **Odoo**: 18.0
- **Autor**: DICC - Desarrollo e Innovación 