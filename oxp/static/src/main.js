/** @odoo-module **/

import { mount, whenReady} from "@odoo/owl";
import { Page } from "./page";
import { templates } from "@web/core/assets";

//Monta en componente en la pagina cuando document.body a sido cargado
whenReady (()=>{
    mount(Page, document.body, {templates,dev:true,name:"Ola odooers y diccquers"});
});