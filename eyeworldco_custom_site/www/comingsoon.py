# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals

import frappe
from frappe.utils import now
from frappe import _

no_cache = 1
no_sitemap = 1

def get_context(context):
	context.doc = frappe.get_doc("Website Coming Soon Settings", "Website Coming Soon Settings")
	
	context.title = context.doc.title

	return context


