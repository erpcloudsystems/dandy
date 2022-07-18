from __future__ import unicode_literals
import frappe
from frappe import _


@frappe.whitelist()
def before_insert(doc, method=None):
    pass
@frappe.whitelist()
def after_insert(doc, method=None):
    pass
@frappe.whitelist()
def onload(doc, method=None):
    pass
@frappe.whitelist()
def before_validate(doc, method=None):
    pass
@frappe.whitelist()
def validate(doc, method=None):
    pass
@frappe.whitelist()
def on_submit(doc, method=None):
    repayment_schedule = frappe.get_doc('PMS Repayment Schedule', {'name': doc.row_name, 'parent': doc.reference_link})
    repayment_schedule.electricity_paid = 1
    repayment_schedule.save()
@frappe.whitelist()
def on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def before_save(doc, method=None):
    pass
@frappe.whitelist()
def before_cancel(doc, method=None):
    repayment_schedule = frappe.get_doc('PMS Repayment Schedule', {'name': doc.row_name, 'parent': doc.reference_link})
    repayment_schedule.electricity_paid = 0
    repayment_schedule.save()
@frappe.whitelist()
def on_update(doc, method=None):
    pass
