/** @odoo-module **/
import { ProductListPage } from "@pos_self_order/app/pages/product_list_page/product_list_page";
import { patch } from "@web/core/utils/patch";

patch(ProductListPage.prototype, {
    setup() {
        super.setup();
        console.log("ProductListPage Search Patch Applied XXX"); // Mensaje para depuración
        this.searchState = {
            isVisible: false,
            input: "",
        };
    },

    focusSearch() {
        this.searchState.isVisible = !this.searchState.isVisible;
        if (!this.searchState.isVisible) {
            this.searchState.input = "";
        }
        this.render();
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