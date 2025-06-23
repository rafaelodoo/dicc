/** @odoo-module */

import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { patch } from "@web/core/utils/patch";

// Este es el parche más simple posible.
// Heredamos el método setup, que es el primero en ejecutarse en un componente.
patch(ProductScreen.prototype, {
    setup() {
        // Es CRUCIAL llamar al setup original primero.
        super.setup();

        // Esta es nuestra prueba. Si este mensaje aparece, la conexión funciona.
        console.log("*************************************************");
        console.log("* ¡HOLA DESDE EL PARCHE! ¡El JS se ha cargado! *");
        console.log("*************************************************");
    }
});