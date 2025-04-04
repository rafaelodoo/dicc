/** @odoo-module **/
import { ProductListPage } from "@pos_self_order/app/pages/product_list_page/product_list_page";
import { patch } from "@web/core/utils/patch";

patch(ProductListPage.prototype, {
    setup() {
        super.setup();
        this.state.search = false;
        this.state.searchInput = "";
    },

    focusSearch() {
        this.state.search = !this.state.search;
        if (!this.state.search) {
            this.state.searchInput = "";
        }
    },

    getFilteredProducts(products) {
        const searchInput = this.state.searchInput.toLowerCase();
        return products.filter(product => 
            product.name.toLowerCase().includes(searchInput) ||
            (product.description_self_order && product.description_self_order.toLowerCase().includes(searchInput))
        );
    }
}); 