{
    "name": "Mi componente de eLearning",
    "author": "CampusCleverit",
    "website": "https://campuscleverit.es",
    "version": "18.0.0.1.0",
    "summary": "Displays subscribed eLearning courses on the portal using OWL",
    "category": "Portal/eLearning",
    "depends": [
        "portal",
        "website_slides",
        "web"
    ],
    "data": [
        "views/portal_template.xml"
    ],
    "assets": {
        "web.assets_frontend": [
            "elearning_portal/static/src/components/*.js",
            "elearning_portal/static/src/components/*.xml"
        ]
    },
    
    "application": false,
    "auto_install": false,
    "license": "LGPL-3"
}