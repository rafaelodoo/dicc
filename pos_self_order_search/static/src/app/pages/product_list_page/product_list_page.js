/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { ProductListPage } from "@pos_self_order/app/pages/product_list_page/product_list_page";
import { useState } from "@odoo/owl";

// Parcheamos el prototipo del componente original ProductListPage
patch(ProductListPage.prototype, {
    // Sobrescribimos el método setup para inicializar el estado de búsqueda
    setup() {
        // Llamamos al setup original para mantener su funcionalidad
        super.setup(...arguments);

        // Añadimos un nuevo estado reactivo para almacenar el término de búsqueda
        this.searchState = useState({ term: "" });
    },

    // Creamos la función que se llamará desde el input en el XML
    onSearchInput(event) {
        // Actualizamos el término de búsqueda en nuestro estado.
        // Lo convertimos a minúsculas para búsqueda insensible a mayúsculas/minúsculas.
        this.searchState.term = event.target.value.toLowerCase();
    },

    // Sobrescribimos el getter 'products' que calcula la lista de productos a mostrar
    get products() {
        // Obtenemos la lista de productos original (ya filtrada por categoría si aplica)
        // llamando al getter original usando 'super'.
        const originalProducts = super.products;

        // Si no hay término de búsqueda, devolvemos la lista original sin cambios
        if (!this.searchState.term) {
            return originalProducts;
        }

        // Si hay un término de búsqueda, filtramos la lista original
        const searchTerm = this.searchState.term;
        return originalProducts.filter(product =>
            // Comprobamos si el nombre del producto (en minúsculas) incluye el término de búsqueda
            // También podríamos incluir otros campos como 'barcode' si fuera necesario:
            // (product.display_name.toLowerCase().includes(searchTerm) ||
            //  (product.barcode && product.barcode.toLowerCase().includes(searchTerm)))
            product.display_name.toLowerCase().includes(searchTerm)
        );
    }
});