/** @odoo-module **/

import { SelfOrderScreen } from "@pos_self_order/self_order/SelfOrderScreen";
import { useService } from "@web/core/utils/hooks";
import { useState } from "@odoo/owl";
import { debounce } from "@web/core/utils/timing";

export class SelfOrderScreenWithSearch extends SelfOrderScreen {
    setup() {
        super.setup();
        this.orm = useService("orm");
        this.searchState = useState({
            searchTerm: "",
            isSearching: false,
            searchResults: [],
        });

        this.debouncedSearch = debounce(this.performSearch, 300);
    }

    async performSearch() {
        if (!this.searchState.searchTerm) {
            this.searchState.searchResults = [];
            return;
        }

        this.searchState.isSearching = true;
        try {
            const results = await this.orm.call(
                "pos.session",
                "search_products_for_self_order",
                [this.searchState.searchTerm]
            );
            this.searchState.searchResults = results;
        } catch (error) {
            console.error("Error searching products:", error);
            this.searchState.searchResults = [];
        } finally {
            this.searchState.isSearching = false;
        }
    }

    onSearchInput(ev) {
        this.searchState.searchTerm = ev.target.value;
        this.debouncedSearch();
    }

    get productsToDisplay() {
        if (this.searchState.searchTerm) {
            return this.searchState.searchResults;
        }
        return super.productsToDisplay;
    }
} 