import odoo
import odoo.http as http
from odoo.http import request

class PortalElearningController(http.Controller):
    @http.route("/my_portal/subscribed_courses", type="json", auth="user", website=True)
    def get_subscribed_courses(self, partner_id=None, **kw):
        current_user_partner_id = request.env.user.partner_id.id
        if not partner_id or partner_id != current_user_partner_id:
            return []
        return self._fetch_courses_for_partner(partner_id)

    def _fetch_courses_for_partner(self, partner_id):
        try:
            subscriptions = (
                request.env["slide.channel.partner"]
                .sudo()
                .search([("partner_id", "=", partner_id)])
            )
            channel_ids = subscriptions.mapped("channel_id").ids
            courses = (
                request.env["slide.channel"]
                .sudo()
                .search_read([("id", "in", channel_ids)], ["id", "name"])
            )
            return courses
        except Exception as e:
            odoo.exceptions.UserError(f"Error fetching subscribed courses: {e}")
            return []