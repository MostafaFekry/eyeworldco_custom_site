# -*- coding: utf-8 -*-
# Copyright (c) 2019, MostafaFekry and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class WebsiteComingSoonSettings(Document):
	def on_update(self):
		from frappe.website.render import clear_cache
		clear_cache("comingsoon")


def get_args():
	obj = frappe.get_doc("Website Coming Soon Settings")
	return {
		"obj": obj
	}

