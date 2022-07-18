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
    
    payment_entry_amount = 0
    advanced_amount = 0
    total_paid_amount = 0
    
    if doc.reference_doctype == "PMS Lease Contract" and doc.contract_repayment_schedule == 1:
        repayment_schedule = frappe.get_doc('PMS Repayment Schedule', {'name': doc.row_name, 'parent': doc.reference_link})
        if repayment_schedule.outstanding_amount == 0:
            repayment_schedule.is_paid = 1
        amount = frappe.db.sql(""" select sum(`tabPayment Entry`.paid_amount) as paid_amount
                                   from `tabPayment Entry` 
                                   where `tabPayment Entry`.row_name ='{rowname}'
                                   and `tabPayment Entry`.docstatus =1
                               """.format(name=repayment_schedule.sales_invoice,rowname=doc.row_name), as_dict=1)
        for x in amount:
            payment_entry_amount = x.paid_amount
            repayment_schedule.paid_amount = payment_entry_amount
            
        repayment_schedule.save()
    if doc.reference_doctype == "PMS Lease Contract":
        contract = frappe.get_doc("PMS Lease Contract", doc.reference_link)
        if contract.advanced_paid == 1:  
            advanced_amount = contract.base_advanced_amount
            contract.base_total_amount_paid = total_paid_amount + advanced_amount
            contract.total_amount_paid = contract.base_total_amount_paid / contract.conversion_rate
    
        contract.save()
        if contract.insurance_pe == doc.name:
            contract.insurance_paid = 1
            contract.save()

        if contract.advanced_pe == doc.name:
            contract.advanced_paid = 1
            contract.save()

@frappe.whitelist()
def on_cancel(doc, method=None):
    
    payment_entry_amount = 0
    advanced_amount = 0
    total_paid_amount = 0
    total_invoice = 0
    if doc.reference_doctype == "PMS Lease Contract" and doc.contract_repayment_schedule == 1 and doc.docstatus == 0:
        repayment_schedule = frappe.get_doc('PMS Repayment Schedule', {'name': doc.row_name, 'parent': doc.reference_link})
        if repayment_schedule.outstanding_amount > 0:
            repayment_schedule.is_paid == 0
        amount =  frappe.db.sql(""" select sum(`tabPayment Entry`.paid_amount) as paid_amount
                                   from `tabPayment Entry` 
                                   where `tabPayment Entry`.row_name ='{rowname}'
                                   and `tabPayment Entry`.docstatus =1
                               """.format(name=repayment_schedule.sales_invoice,rowname=doc.row_name), as_dict=1)
        for x in amount:
            payment_entry_amount = x.paid_amount
            repayment_schedule.paid_amount = payment_entry_amount
        repayment_schedule.save()
    if doc.reference_doctype == "PMS Lease Contract":
        contract = frappe.get_doc("PMS Lease Contract", doc.reference_link)
        if contract.advanced_paid == 1:  
            advanced_amount = contract.base_advanced_amount
            contract.base_total_amount_paid = total_paid_amount + advanced_amount
            contract.total_amount_paid = contract.base_total_amount_paid / contract.conversion_rate
            contract.save()
        if contract.insurance_pe == doc.name:
            contract.insurance_paid = 0
            contract.insurance_pe = ""
            contract.save()

        if contract.advanced_pe == doc.name:
            contract.advanced_paid = 0
            contract.advanced_pe = ""
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
