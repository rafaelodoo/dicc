# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError


class TestPosSessionSearch(TransactionCase):
    
    def setUp(self):
        super(TestPosSessionSearch, self).setUp()
        
        # Crear categoría de prueba
        self.category = self.env['product.category'].create({
            'name': 'Categoria Test'
        })
        
        # Crear productos de prueba
        self.product1 = self.env['product.product'].create({
            'name': 'Producto Coca Cola',
            'default_code': 'COCA001',
            'available_in_pos': True,
            'sale_ok': True,
            'lst_price': 2.50,
            'categ_id': self.category.id,
        })
        
        self.product2 = self.env['product.product'].create({
            'name': 'Pepsi Cola',
            'default_code': 'PEPSI002',
            'available_in_pos': True,
            'sale_ok': True,
            'lst_price': 2.30,
            'categ_id': self.category.id,
        })
        
        # Producto NO disponible en PdV
        self.product3 = self.env['product.product'].create({
            'name': 'Producto No Disponible',
            'default_code': 'NODISP003',
            'available_in_pos': False,
            'sale_ok': True,
            'lst_price': 1.50,
            'categ_id': self.category.id,
        })
        
        # Crear POS Session para usar en tests
        self.pos_session = self.env['pos.session'].create({
            'config_id': self.env.ref('point_of_sale.pos_config_main').id,
            'user_id': self.env.user.id,
        })
    
    def test_search_by_name_case_insensitive(self):
        """Test: Buscar por nombre insensible a mayúsculas"""
        # Buscar "coca" en minúsculas
        result = self.pos_session.search_products_for_self_order('coca')
        
        # Debe encontrar el producto1 (Coca Cola)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['id'], self.product1.id)
        self.assertEqual(result[0]['name'], 'Producto Coca Cola')
        
        # Buscar "COCA" en mayúsculas (debe encontrar el mismo)
        result = self.pos_session.search_products_for_self_order('COCA')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['id'], self.product1.id)
    
    def test_search_by_default_code(self):
        """Test: Buscar por código interno (default_code)"""
        result = self.pos_session.search_products_for_self_order('PEPSI002')
        
        # Debe encontrar el product2
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['id'], self.product2.id)
        self.assertEqual(result[0]['default_code'], 'PEPSI002')
    
    def test_search_multiple_results(self):
        """Test: Buscar término que coincida con múltiples productos"""
        result = self.pos_session.search_products_for_self_order('cola')
        
        # Debe encontrar ambos productos (Coca Cola y Pepsi Cola)
        self.assertEqual(len(result), 2)
        product_ids = [p['id'] for p in result]
        self.assertIn(self.product1.id, product_ids)
        self.assertIn(self.product2.id, product_ids)
    
    def test_search_no_results(self):
        """Test: Query sin coincidencias debe retornar lista vacía"""
        result = self.pos_session.search_products_for_self_order('producto_inexistente')
        
        # Debe retornar lista vacía
        self.assertEqual(result, [])
        self.assertIsInstance(result, list)
    
    def test_filter_available_in_pos_only(self):
        """Test: Solo debe retornar productos con available_in_pos = True"""
        # Buscar por un término que coincida con el producto NO disponible
        result = self.pos_session.search_products_for_self_order('NODISP003')
        
        # No debe encontrar nada porque available_in_pos = False
        self.assertEqual(result, [])
        
        # Cambiar el producto a disponible y volver a buscar
        self.product3.available_in_pos = True
        result = self.pos_session.search_products_for_self_order('NODISP003')
        
        # Ahora sí debe encontrarlo
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['id'], self.product3.id)
    
    def test_search_invalid_query(self):
        """Test: Query inválida debe retornar lista vacía"""
        # Query vacía
        result = self.pos_session.search_products_for_self_order('')
        self.assertEqual(result, [])
        
        # Query None
        result = self.pos_session.search_products_for_self_order(None)
        self.assertEqual(result, [])
        
        # Query con solo espacios
        result = self.pos_session.search_products_for_self_order('   ')
        self.assertEqual(result, [])
    
    def test_returned_data_structure(self):
        """Test: Estructura de datos retornados"""
        result = self.pos_session.search_products_for_self_order('coca')
        
        self.assertEqual(len(result), 1)
        product_data = result[0]
        
        # Verificar campos obligatorios
        required_fields = [
            'id', 'display_name', 'name', 'default_code', 'lst_price',
            'standard_price', 'available_in_pos', 'sale_ok', 'active'
        ]
        
        for field in required_fields:
            self.assertIn(field, product_data)
        
        # Verificar tipos de datos
        self.assertIsInstance(product_data['id'], int)
        self.assertIsInstance(product_data['name'], str)
        self.assertIsInstance(product_data['available_in_pos'], bool)
        self.assertTrue(product_data['available_in_pos'])  # Debe ser True
    
    def test_endpoint_accessibility(self):
        """Test: El endpoint RPC es accesible desde pos.session"""
        # Verificar que el método existe en el modelo
        self.assertTrue(hasattr(self.pos_session, 'search_products_for_self_order'))
        
        # Verificar que es callable
        self.assertTrue(callable(getattr(self.pos_session, 'search_products_for_self_order')))
        
        # Verificar que se puede llamar sin errores
        result = self.pos_session.search_products_for_self_order('test')
        self.assertIsInstance(result, list) 