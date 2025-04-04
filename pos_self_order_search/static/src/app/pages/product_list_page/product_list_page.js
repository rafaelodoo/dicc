/** @odoo-module **/
import { ProductListPage } from "@pos_self_order/app/pages/product_list_page/product_list_page";
import { patch } from "@web/core/utils/patch";
import { useRef } from "@odoo/owl";

patch(ProductListPage.prototype, {
    setup() {
        super.setup();
        this.searchState = {
            isVisible: false,
            input: "",
        };
        this.searchInputRef = useRef("searchInput");
    },

    focusSearch() {
        this.searchState.isVisible = !this.searchState.isVisible;
        if (!this.searchState.isVisible) {
            this.searchState.input = "";
        } else {
            // Focus the input field when showing the search
            requestAnimationFrame(() => {
                if (this.searchInputRef.el) {
                    this.searchInputRef.el.focus();
                }
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