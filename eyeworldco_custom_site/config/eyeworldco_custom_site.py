from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Web Site"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Web Page",
					"description": _("Content web page."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Web Form",
					"description": _("User editable form on Website."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Website Slideshow",
					"description": _("Embed image slideshows in website pages."),
				},
				{
					"type": "doctype",
					"name": "Website Route Meta",
					"description": _("Add meta tags to your web pages"),
				},
			]
		},
		{
			"label": _("Setup"),
			"icon": "fa fa-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Website Settings",
					"description": _("Setup of top navigation bar, footer and logo."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Eye World Website Settings",
					"description": _("Setup of Eye World Website Settings."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Website Social Media",
					"description": _("List of Website Social Media."),
				},
				{
					"type": "doctype",
					"name": "Website Coming Soon Settings",
					"description": _("Settings for Coming Soon Page."),
				},
			]
		},
		{
			"label": _("Reservation Setup"),
			"icon": "fa fa-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Reservation Settings",
					"description": _("Setup of Reservation."),
					"onboard": 1,
				},
			]
		},

	]