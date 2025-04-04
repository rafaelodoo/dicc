/** @odoo-module **/
import { ProductListPage } from "@pos_self_order/app/pages/product_list_page/product_list_page";
import { patch } from "@web/core/utils/patch";
import { useComponent } from "@odoo/owl";

patch(ProductListPage.prototype, {
    setup() {
        super.setup();
        const component = useComponent();
        component.searchState = {
            isVisible: false,
            input: "",
        };
    },

    focusSearch() {
        const component = useComponent();
        component.searchState.isVisible = !component.searchState.isVisible;
        if (!component.searchState.isVisible) {
            component.searchState.input = "";
        }
        component.render();
    },

    getFilteredProducts(products) {
        const component = useComponent();
        const searchInput = component.searchState.input.toLowerCase();
        if (!searchInput) {
            return products;
        }
        return products.filter(product => 
            product.name.toLowerCase().includes(searchInput) ||
            (product.description_self_order && product.description_self_order.toLowerCase().includes(searchInput))
        );
    }
}); 