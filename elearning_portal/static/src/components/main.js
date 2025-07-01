import { Component, useState, onWillStart } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { rpc } from "@web/core/network/rpc";

console.log("elearning_portal: subscribed_courses.js loaded");

export class SubscribedCourses extends Component {
  static template = "elearning_portal.SubscribedCoursesTemplate";

  static props = {
    partnerId: { type: [Number, Boolean] },
  };

  setup() {
    this.state = useState({
      courses: [],
      isLoading: true,
      error: null,
    });

    onWillStart(async () => {
      if (!this.props.partnerId) {
        console.warn("Partner ID not provided.");
        this.state.isLoading = false;
        this.state.error = "Could not identify the user.";
        return;
      }
      await this.loadSubscribedCourses();
    });
  }

  async loadSubscribedCourses() {
    this.state.isLoading = true;
    this.state.error = null;
    try {
      const result = await rpc("/my_portal/subscribed_courses", {
        partner_id: this.props.partnerId,
      });
      this.state.courses = result;
      console.log("Courses loaded:", this.state.courses);
    } catch (err) {
      console.error("Error loading subscribed courses:", err);
      this.state.error = "An error occurred while loading your courses.";
    } finally {
      this.state.isLoading = false;
      const h3_it = document.querySelector("h3.h3_portal_courses");
      h3_it.textContent = `Mis cursos odooers (${this.state.courses.length})`;
    }
  }
}

registry
  .category("public_components")
  .add("elearning_portal.SubscribedCourses", SubscribedCourses);