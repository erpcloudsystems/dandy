# Copyright (c) 2022, ERP Cloud Systems and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document

class Staranalytics(Document):
	@frappe.whitelist()
	def validate(self):
		subtotal = 0
		for x in self.star_analytics_table:
			subtotal += x.sub_total
			nettotal += x.net_total
		self.totals_sub_total = subtotal
		self.totals_net_total = nettotal
		'''
		subtotal = frappe.db.sql("""
									SELECT 
										sum(`tabStar analytics Table`.sub_total) as sub_total,
										FROM
										`tabStar analytics Table`  join `tabStar analytics` on `tabStar analytics`.name = `tabStar analytics Table`.parent 
										where `tabStar analytics`.name = '{name}'
										 """.format(name=self.name), as_dict=1)
		self.sub_total = subtotal

		discount = frappe.db.sql("""
									SELECT 
										sum(`tabStar analytics Table`.discount) as discount,
										FROM
										`tabStar analytics Table`  join `tabStar analytics` on `tabStar analytics`.name = `tabStar analytics Table`.parent 
										where `tabStar analytics`.name = '{name}'
										 """.format(name=self.name), as_dict=1)
		self.discount = discount

		services = frappe.db.sql("""
									SELECT 
										sum(`tabStar analytics Table`.services) as services,
										FROM
										`tabStar analytics Table`  join `tabStar analytics` on `tabStar analytics`.name = `tabStar analytics Table`.parent 
										where `tabStar analytics`.name = '{name}'
										 """.format(name=self.name), as_dict=1)
		self.services = services

		taxes = frappe.db.sql("""
								SELECT 
									sum(`tabStar analytics Table`.taxes) as services,
									FROM
									`tabStar analytics Table`  join `tabStar analytics` on `tabStar analytics`.name = `tabStar analytics Table`.parent 
									where `tabStar analytics`.name = '{name}'
									 """.format(name=self.name), as_dict=1)
		self.taxes = taxes

		nettotal = frappe.db.sql("""
									SELECT 
										sum(`tabStar analytics Table`.net_total) as services,
										FROM
										`tabStar analytics Table`  join `tabStar analytics` on `tabStar analytics`.name = `tabStar analytics Table`.parent 
										where `tabStar analytics`.name = '{name}'
										 """.format(name=self.name), as_dict=1)
		self.net_total = nettotal
		'''