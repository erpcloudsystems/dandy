# Copyright (c) 2022, ERP Cloud Systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RevenueShareTransaction(Document):
		@frappe.whitelist()
		def validate(self):
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
		