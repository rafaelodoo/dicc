/** @odoo-module */

import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { CustomerNoteButton } from "@pos_customer_note/app/components/customer_note_button/customer_note_button";
import { patch } from "@web/core/utils/patch";

// Usamos patch para añadir nuestro componente a la lista de componentes de ProductScreen
patch(ProductScreen.components, {
    CustomerNoteButton,
});