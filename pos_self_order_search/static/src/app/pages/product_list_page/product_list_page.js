/** @odoo-module **/
import { ProductListPage } from "@pos_self_order/app/pages/product_list_page/product_list_page";
import { patch } from "@web/core/utils/patch";
import { useRef, useState } from "@odoo/owl";

patch(ProductListPage.prototype, {
    setup() {
        super.setup();
        this.searchState = useState({
            isVisible: false,
            input: "",
        });
        this.searchInputRef = useRef("searchInput");
    },

    toggleSearch(ev) {
        ev.preventDefault();
        ev.stopPropagation();
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
    },

    onInputSearch(ev) {
        this.searchState.input = ev.target.value;
    },

    getFilteredProducts(products) {
        if (!Array.isArray(products)) {
            return [];
        }
        const searchInput = this.searchState.input.toLowerCase().trim();
        if (!searchInput) {
            return products;
        }
        return products.filter(product => {
            const name = (product.name || "").toLowerCase();
            const description = (product.description_self_order || "").toLowerCase();
            return name.includes(searchInput) || description.includes(searchInput);
        });
    }
}); 