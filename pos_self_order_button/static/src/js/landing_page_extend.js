/** @odoo-module **/

import { LandingPage } from "@pos_self_order/static/src/app/pages/landing_page/landing_page";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";

patch(LandingPage, 'pos_self_order_button.LandingPage', {
    setup() {
        this._super.setup();
        this.action = useService("action"); // Usamos el servicio 'action' para manejar las acciones del botón
    },

    // Método para manejar el clic del botón
    async _onClickMyCustomButton() {
        // Aquí puedes añadir la lógica de tu botón
        // Por ejemplo, mostrar una alerta:
        // alert("¡Botón personalizado clickeado!");

        // O ejecutar una acción de Odoo:
        // this.action.doAction({
        //     type: 'ir.actions.act_window',
        //     name: 'Mi Ventana Personalizada',
        //     res_model: 'mi.modelo',
        //     view_mode: 'tree,form',
        // });
        alert("¡Botón personalizado clickeado!");
    },
});