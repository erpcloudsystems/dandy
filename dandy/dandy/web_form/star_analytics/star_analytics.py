from __future__ import unicode_literals

import frappe

def get_context(context):
	# do your magic here
	frappe.web_form.after_load = () => {
    frappe.msgprint('Please fill all values carefully');
}