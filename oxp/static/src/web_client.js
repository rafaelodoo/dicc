/** @odoo-module **/

import { Component } from "@odoo/owl";
import { Navbar } from "./nabvar";

export class WebClient extends Component {
    static template = "oxn.Webclient";
    static components = { Navbar };
}
