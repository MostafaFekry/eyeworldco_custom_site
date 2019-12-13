# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "eyeworldco_custom_site"
app_title = "Eyeworldco Custom Site"
app_publisher = "MostafaFekry"
app_description = "Custom app to Eye of the world Site"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "mostafa.fekry@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/eyeworldco_custom_site/css/eyeworldco_custom_site.css"
# app_include_js = "/assets/eyeworldco_custom_site/js/eyeworldco_custom_site.js"

# include js, css files in header of web template
# web_include_css = "/assets/eyeworldco_custom_site/css/eyeworldco_custom_site.css"
# web_include_js = "/assets/eyeworldco_custom_site/js/eyeworldco_custom_site.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "eyeworldco_custom_site.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# website
update_website_context = "eyeworldco_custom_site.utils.update_website_context"

# before_install = "eyeworldco_custom_site.install.before_install"
# after_install = "eyeworldco_custom_site.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "eyeworldco_custom_site.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"eyeworldco_custom_site.tasks.all"
# 	],
# 	"daily": [
# 		"eyeworldco_custom_site.tasks.daily"
# 	],
# 	"hourly": [
# 		"eyeworldco_custom_site.tasks.hourly"
# 	],
# 	"weekly": [
# 		"eyeworldco_custom_site.tasks.weekly"
# 	]
# 	"monthly": [
# 		"eyeworldco_custom_site.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "eyeworldco_custom_site.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "eyeworldco_custom_site.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "eyeworldco_custom_site.task.get_dashboard_data"
# }


# fixtures
fixtures = [{"dt": "Custom Field", "filters": [["name", "in", [
		"Item-reserved",
		"Sales Order-sales_order_reserved"
	]]]},
    {"dt": "Custom Script", "filters": [["name", "in", [
		"Quotation-Client",
		"Sales Order-Client"
    ]]]},
    {"dt": "Website Social Media"},
    {"dt": "Website Coming Soon Settings"}
	]
