# Copyright (c) 2022, ERP Cloud Systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import datetime


class RevenueShareTransaction(Document):
	@frappe.whitelist()
	def validate(self):
		if self.revenue_share_transaction_details:
			subtotal = 0
			nettotal = 0
			discount = 0
			services = 0
			taxes = 0
			count_of_checks = len(self.get("revenue_share_transaction_details"))

			for x in self.revenue_share_transaction_details:
				subtotal += x.sub_total
				nettotal += x.net_total
				discount += x.discount
				services += x.services
				taxes += x.taxes
			self.totals_sub_total = subtotal
			self.totals_net_total = nettotal
			self.totals_discount = discount
			self.totals_services = services
			self.totals_taxes = taxes
			self.count_of_checks = count_of_checks

		
	@frappe.whitelist()
	def on_submit(self):
		transaction = frappe.db.sql(""" select (select sum(`tabRevenue Share Transaction`.totals_net_total) 
												from `tabRevenue Share Transaction` 
												where MONTH(`tabPMS Repayment Schedule`.payment_date) = MONTH(`tabRevenue Share Transaction`.date)
												and YEAR(`tabPMS Repayment Schedule`.payment_date) = YEAR(`tabRevenue Share Transaction`.date) 
												and `tabPMS Repayment Schedule`.parent = `tabRevenue Share Transaction`.pms_lease_contract
												and `tabRevenue Share Transaction`.docstatus = 1) as total,
										`tabPMS Repayment Schedule`.name as row
										from `tabPMS Repayment Schedule` join `tabRevenue Share Transaction` on `tabPMS Repayment Schedule`.parent = `tabRevenue Share Transaction`.pms_lease_contract 
										
									""", as_dict=1)

		for x in transaction:
			z = frappe.get_doc('PMS Repayment Schedule', x.row)
			z.revenue_share_total = x.total
			z.save()