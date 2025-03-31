/** @odoo-module **/

// Importaciones necesarias
import { patch } from "@web/core/utils/patch"; // Utilidad para parchear
// import { ProductListPage } from "@pos_self_order/app/pages/product_list_page/product_list_page"; 
import { ProductListPage } from "@pos_self_order/static/src/app/pages/product_list_page/product_list_page"; // Componente original
import { useState } from "@odoo/owl"; // Hook para estado reactivo

// Aplicamos el parche al prototipo del componente original
patch(ProductListPage.prototype, {

    /**
     * Sobrescribimos el método setup para añadir nuestro estado de búsqueda.
     */
    setup() {
        // MUY IMPORTANTE: Llamar al setup original primero
        super.setup(...arguments);

        // Inicializamos el estado para guardar el término de búsqueda
        // useState hace que la interfaz reaccione a los cambios en searchState.term
        this.searchState = useState({ term: "" });

        console.log("ProductListPage Search Patch Applied"); // Mensaje para depuración
    },

    /**
     * Manejador para el evento 'input' de nuestra barra de búsqueda.
     * Se ejecuta cada vez que el usuario escribe algo.
     * @param {Event} event El evento del DOM
     */
    onSearchInput(event) {
        // Actualizamos el término de búsqueda en el estado.
        // Convertimos a minúsculas para búsqueda no sensible a mayúsculas.
        this.searchState.term = event.target.value.toLowerCase();
        // console.log("Search term:", this.searchState.term); // Descomentar para depurar
    },

    /**
     * Sobrescribimos el getter 'products'.
     * Este getter calcula la lista de productos que se mostrarán en la plantilla.
     * Ahora incluirá el filtrado por búsqueda además del filtrado por categoría original.
     */
    get products() {
        // 1. Obtenemos la lista de productos calculada por el componente original
        //    (esto ya incluye el filtrado por categoría, si existe).
        const originalProducts = super.products;

        // 2. Verificamos si hay un término de búsqueda activo.
        const searchTerm = this.searchState.term;
        if (!searchTerm) {
            // Si no hay búsqueda, devolvemos la lista original tal cual.
            return originalProducts;
        }

        // 3. Si hay un término de búsqueda, filtramos la lista original.
        console.log(`Filtering products by: "${searchTerm}"`); // Mensaje para depuración
        const filteredProducts = originalProducts.filter(product =>
            // Comprobamos si el nombre (display_name) del producto en minúsculas
            // incluye el término de búsqueda.
            // Puedes añadir más campos aquí si quieres buscar por código de barras, etc.
            // ej: product.barcode && product.barcode.toLowerCase().includes(searchTerm) || ...
            product.display_name.toLowerCase().includes(searchTerm)
        );
        console.log(`Found ${filteredProducts.length} products`); // Mensaje para depuración
        return filteredProducts; // Devolvemos la lista filtrada.
    }
});