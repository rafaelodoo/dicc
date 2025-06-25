/** @odoo-module */

import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { patch } from "@web/core/utils/patch";
import { CustomerNoteButton } from "../../components/customer_note_button/customer_note_button";

patch(ProductScreen.prototype, {
    // Agregar el botón a la barra de control
    get controlButtons() {
        const buttons = super.controlButtons || [];
        return [
            ...buttons,
            {
                component: CustomerNoteButton,
                key: 'customer_note',
            },
        ];
    },
});