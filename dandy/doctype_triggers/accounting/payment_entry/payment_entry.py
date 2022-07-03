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
    
    if doc.contract_repayment_schedule == 1:
        repayment_schedule = frappe.get_doc('PMS Repayment Schedule', {'name': doc.row_name, 'parent': doc.reference_link})
   
        amount =  frappe.db.sql(""" select a.allocated_amount, a.outstanding_amount
                                   from `tabPayment Entry Reference` a join `tabPayment Entry` b
                                   on a.parent = b.name
                                   where a.reference_name = '{name}'
                                   and b.row_name ='{rowname}'
                                   and b.docstatus =1
                               """.format(name=repayment_schedule.sales_invoice,rowname=doc.row_name), as_dict=1)
        for x in amount:
            payment_entry_amount += x.allocated_amount
        repayment_schedule.paid_amount = payment_entry_amount
        repayment_schedule.outstanding_amount = x.outstanding_amount
        
        repayment_schedule.save()
    if doc.reference_doctype == "PMS Lease Contract":
        contract = frappe.get_doc("PMS Lease Contract", doc.reference_link)
        
       
        paid_amount =  frappe.db.sql(""" select a.name, a.paid_amount,a.invoice_amount
                                   from `tabPMS Repayment Schedule` a join `tabPMS Lease Contract` b
                                   on a.parent = b.name
                                   where b.name = '{name}'
                                   
                               """.format(name=contract.name), as_dict=1)
        for x in paid_amount:
            total_paid_amount += float(x.paid_amount)
            contract.base_total_amount_paid = total_paid_amount
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
    
    if doc.contract_repayment_schedule == 1:
        repayment_schedule = frappe.get_doc('PMS Repayment Schedule', {'name': doc.row_name, 'parent': doc.reference_link})
   
        amount =  frappe.db.sql(""" select a.allocated_amount, a.outstanding_amount, a.total_amount
                                   from `tabPayment Entry Reference` a join `tabPayment Entry` b
                                   on a.parent = b.name
                                   where b.row_name = '{name}'
                                   and b.docstatus =1
                               """.format(name=doc.row_name), as_dict=1)
        for x in amount:
            payment_entry_amount += x.allocated_amount
        repayment_schedule.paid_amount = payment_entry_amount
        
        
        repayment_schedule.save()
    if doc.reference_doctype == "PMS Lease Contract":
        contract = frappe.get_doc("PMS Lease Contract", doc.reference_link)
        paid_amount =  frappe.db.sql(""" select a.name, a.paid_amount,a.invoice_amount
                                   from `tabPMS Repayment Schedule` a join `tabPMS Lease Contract` b
                                   on a.parent = b.name
                                   where b.name = '{name}'
                                   
                               """.format(name=contract.name), as_dict=1)
        for x in paid_amount:
            total_paid_amount += float(x.paid_amount)
            contract.base_total_amount_paid = total_paid_amount
            if contract.advanced_paid == 1:  
                advanced_amount = contract.base_advanced_amount
                contract.base_total_amount_paid = total_paid_amount + advanced_amount
            contract.total_amount_paid = contract.base_total_amount_paid / contract.conversion_rate
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
