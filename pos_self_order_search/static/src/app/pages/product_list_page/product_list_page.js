/** @odoo-module **/
import { ProductListPage } from "@pos_self_order/app/pages/product_list_page/product_list_page";
import { patch } from "@web/core/utils/patch";
import { useState } from "@web/core/utils/hooks";

patch(ProductListPage.prototype, {
    setup() {
        super.setup();
        this.searchState = useState({
            isVisible: false,
            input: "",
        });
    },

    focusSearch() {
        this.searchState.isVisible = !this.searchState.isVisible;
        if (!this.searchState.isVisible) {
            this.searchState.input = "";
        }
    },

    getFilteredProducts(products) {
        const searchInput = this.searchState.input.toLowerCase();
        if (!searchInput) {
            return products;
        }
        return products.filter(product => 
            product.name.toLowerCase().includes(searchInput) ||
            (product.description_self_order && product.description_self_order.toLowerCase().includes(searchInput))
        );
    }
}); 