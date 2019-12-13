# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import throw, msgprint, _
from frappe.utils import get_request_site_address, encode, comma_and
from frappe.model.document import Document

def update_website_context(context):
	website_settings = frappe.get_doc('Eye World Website Settings')
	
	context["main_page_title"] = website_settings.main_page_title
	context["slogan"] = website_settings.slogan
	context["contact_us_hotline"] = website_settings.contact_us_hotline
	context["website_social_media_item"] = website_settings.website_social_media_item


def check_to_make_action(doc, make_action):
	# If not authorized person raise exception
	reservation_settings = frappe.get_doc('Reservation Settings')
	reservation_controller = reservation_settings.reservation_controller
	reserved_item_group = reservation_settings.reserved_item_group
	if not reservation_controller or reservation_controller not in frappe.get_roles():
		throw(_("Please contact to the user who have Sales Master Manager {0} role")
			.format(" / " + reservation_controller if reservation_controller else ""))
	if not reserved_item_group:
		throw(_("Please set Item Group in Reservation Settings"))
		
	li = []
	sales_order_item = get_sales_order_item(doc.name)
	if sales_order_item and reserved_item_group:
		for child_item in sales_order_item:
			for item_group in reserved_item_group:
				if item_group.get("item_group_name") == child_item.get("item_group"):
					item = frappe.get_doc('Item', child_item.get("item_code"))
					if make_action == "Make Reserve Item" and doc.sales_order_reserved == 0:
						item.reserved = 1
					if make_action == "Make Release Item" and doc.sales_order_reserved == 1:
						item.reserved = 0
					item.flags.ignore_validate_update_after_submit = True
					item.save()
					li.append("{0} on row {1}".format(child_item.get("item_code"), child_item.get("idx")))
	
	message = '<br>' + '<br>'.join(li)
	if make_action == "Make Reserve Item" and doc.sales_order_reserved == 0:
		doc.db_set('sales_order_reserved', 1)
		doc.submit()
		msgprint(_("Item/s reserved:{0}").format(comma_and(message)))
	if make_action == "Make Release Item" and doc.sales_order_reserved == 1:
		doc.db_set('sales_order_reserved', 0)
		doc.submit()
		msgprint(_("Item/s Released:{0}").format(comma_and(message)))
		
	#frappe.throw(_("Error:  make_action ({0}),make_action ({1}), make_action ({2})").format(doc.name,make_action,reservation_settings.reserved_item_group))	
	return message
	

def get_sales_order_item(reference_name):
	child_item_name = frappe.get_all("Sales Order Item",
		fields=["item_code","name","idx","item_group"],
		filters={"parent": reference_name}, order_by="idx asc")
	return child_item_name
	
@frappe.whitelist()
def make_reserve_action(reference_doctype, reference_name, make_action):
	
	if not frappe.has_permission(reference_doctype, "write"):
		frappe.throw(_("Not permitted"), frappe.PermissionError)

	doc = frappe.get_doc(reference_doctype, reference_name)
	return check_to_make_action(doc, make_action)






















