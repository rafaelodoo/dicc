/** @odoo-module */

import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";

export class CustomerNoteButton extends Component {
    static template = "pos_customer_note.CustomerNoteButton";

    setup() {
        super.setup();
        this.pos = usePos();
    }

    get partner() {
        return this.pos.get_order().get_partner();
    }

    async onClick() {
        // En la próxima lección, aquí mostraremos el pop-up.
        // Por ahora, solo mostraremos la nota en la consola del navegador.
        if (this.partner && this.partner.comment) {
            console.log("Nota del cliente:", this.partner.comment);
            alert("Nota del Cliente: " + this.partner.comment); // Usamos un alert temporal para que sea visible
        } else {
            console.log("El cliente no tiene notas.");
            alert("El cliente no tiene notas.");
        }
    }
}