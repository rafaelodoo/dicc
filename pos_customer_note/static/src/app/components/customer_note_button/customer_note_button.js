/** @odoo-module */

import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { _t } from "@web/core/l10n/translation";
 
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
        if (this.partner && this.partner.comment) {
            // Mostrar la nota del cliente en un popup
            this.env.services.dialog.alert(
                this.partner.comment,
                {
                    title: _t("Nota del Cliente"),
                    confirm_callback: () => {},
                }
            );
        } else {
            // Mostrar mensaje si no hay nota
            this.env.services.dialog.alert(
                _t("Este cliente no tiene notas internas."),
                {
                    title: _t("Sin Notas"),
                    confirm_callback: () => {},
                }
            );
        }
    }
}