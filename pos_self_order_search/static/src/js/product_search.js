/** @odoo-module **/

import { ProductListPage } from 'pos_self_order.ProductListPage';
import { patch } from "@web/core/utils/patch";
import { useState } from "@odoo/owl";

patch(ProductListPage.prototype, 'pos_self_order_search.ProductListPage', {
    setup() {
        super.setup();
        console.log("ProductListPage patched!"); // <-- Agregado
        this.state = useState({
            searchTerm: '',
            filteredProducts: this.products,
        });
    },

    updateSearchTerm(event) {
        console.log("updateSearchTerm called!"); // <-- Agregado
        this.state.searchTerm = event.target.value;
        this.filterProducts();
    },

    filterProducts() {
        console.log("filterProducts called!"); // <-- Agregado
        if (!this.state.searchTerm) {
            this.state.filteredProducts = this.products;
        } else {
            const term = this.state.searchTerm.toLowerCase();
            this.state.filteredProducts = this.products.filter(product =>
                product.name.toLowerCase().includes(term)
            );
        }
    },

    get productsToDisplay() {
        console.log("productsToDisplay getter called!"); // <-- Agregado
        return this.state.filteredProducts;
    },
});