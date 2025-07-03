{
    "name": "Este es un contador",
    "author": "Rafail López Flores",
    "website": "https://campuscleverit.es",
    "version": "18.0.0.1.0",
    "summary": "Displays subscribed eLearning courses on the portal using OWL",
    "category": "Portal/eLearning",
    "depends": [
        "portal",
        "website_slides",
        "web"
    ],
    "data": [],
    "assets": {
        "web.assets_frontend": [
            "contador/static/src/*.js",
            "contador/static/src/*.scss",
            "contador/static/src/*.xml"
        ]
    },
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3"
}