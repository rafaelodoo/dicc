/** @odoo-module */

import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { CustomerNoteButton } from "@pos_customer_note/app/components/customer_note_button/customer_note_button";
import { patch } from "@web/core/utils/patch";

// Esta es la forma correcta y moderna de añadir un botón de control
patch(ProductScreen.prototype, {
    get controlButtons() {
        // 1. Obtenemos la lista original de botones llamando a super
        const buttons = super.controlButtons;

        // 2. Añadimos nuestro botón a la lista como un objeto de configuración
        buttons.push({
            component: CustomerNoteButton,
            // 3. La condición de visibilidad ahora se define aquí, en el JS
            condition: () => !!this.pos.get_order()?.get_partner(),
        });

        // 4. Devolvemos la lista modificada
        return buttons;
    }
});