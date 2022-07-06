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
   if doc.reference_doctype == "PMS Lease Contract":
        repayment_schedule = frappe.get_doc('PMS Repayment Schedule', {'name': doc.row_name, 'parent': doc.pms_lease_contract})
        repayment_schedule.is_invoiced = 1
        repayment_schedule.sales_invoice = doc.name
        repayment_schedule.invoice_amount = doc.grand_total
        repayment_schedule.save()
        contract = frappe.get_doc("PMS Lease Contract", doc.pms_lease_contract)
        repayment_schedule.save()
        contract.save()

@frappe.whitelist()
def on_cancel(doc, method=None):
    if doc.reference_doctype == "PMS Lease Contract":
        repayment_schedule = frappe.get_doc('PMS Repayment Schedule', {'name': doc.row_name, 'parent': doc.pms_lease_contract})
        repayment_schedule.is_invoiced = 0
        repayment_schedule.sales_invoice = ""
        repayment_schedule.invoice_amount = 0
        repayment_schedule.save()
        contract = frappe.get_doc("PMS Lease Contract", doc.pms_lease_contract)
        contract.save()

@frappe.whitelist()
def on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def before_save(doc, method=None):
    pass
@frappe.whitelist()
def before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def on_update(doc, method=None):
    pass
