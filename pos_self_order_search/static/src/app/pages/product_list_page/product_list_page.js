/** @odoo-module **/
import { ProductListPage } from "@pos_self_order/app/pages/product_list_page/product_list_page";
import { patch } from "@web/core/utils/patch";

patch(ProductListPage.prototype, {
    setup() {
        super.setup();
        this.searchState = {
            isVisible: false,
            input: "",
        };
    },

    focusSearch() {
        this.searchState.isVisible = !this.searchState.isVisible;
        if (!this.searchState.isVisible) {
            this.searchState.input = "";
        } else {
            // Focus the input field when showing the search
            requestAnimationFrame(() => {
                this.refs.searchInput?.focus();
            });
        }
        this.render();
    },

    getFilteredProducts(products) {
        if (!Array.isArray(products)) {
            return [];
        }
        const searchInput = this.searchState.input.toLowerCase().trim();
        if (!searchInput) {
            return products;
        }
        return products.filter(product => 
            (product.name && product.name.toLowerCase().includes(searchInput)) ||
            (product.description_self_order && product.description_self_order.toLowerCase().includes(searchInput))
        );
    }
}); 