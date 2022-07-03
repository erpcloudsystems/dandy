# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe


from __future__ import unicode_literals
import frappe
from frappe import _


def execute(filters=None):
	columns, data = [], []
	columns = get_columns(filters)
	data = get_data(filters, columns)
	return columns, data


def get_columns(filters):
	if filters.get('type') == "Daily":
		return [

			{
				"label": "Revenue Share Transaction",
				"fieldname": "name",
				"fieldtype": "Link",
				"options": "Revenue Share Transaction",
				"width": 100
			},
			{
				"label": "Customer",
				"fieldname": "cust_name",
				"fieldtype": "Link",
				"options": "Customer",
				"width": 180
			},
			{
				"label": "Date",
				"fieldname": "date",
				"fieldtype": "Date",
				"width": 120
			},
			{
				"label": "Store Id",
				"fieldname": "store_id",
				"fieldtype": "Link",
				"options": "Unit",
				"width": 120
			},
			{
				"label": "Zone",
				"fieldname": "zone",
				"fieldtype": "Link",
				"options": "Zone",
				"width": 100
			},
			{
				"label": "Check ID",
				"fieldname": "invc_id",
				"fieldtype": "Data",
				"width": 100
			},
			{
				"label": "Check NO",
				"fieldname": "invc_no",
				"fieldtype": "Data",
				"width": 100
			},
			{
				"label": "Total before tax and service",
				"fieldname": "sub_total",
				"fieldtype": "Currency",
				"width": 150
			},
			{
				"label": "Discount Value",
				"fieldname": "discount",
				"fieldtype": "Currency",
				"width": 120
			},
			{
				"label": "Service Charge",
				"fieldname": "services",
				"fieldtype": "Currency",
				"width": 120
			},
			{
				"label": "Tax Value",
				"fieldname": "taxes",
				"fieldtype": "Currency",
				"width": 120
			},
			{
				"label": "Total Check Value",
				"fieldname": "net_total",
				"fieldtype": "Currency",
				"width": 140
			},
			{
				"label": "Count Of Checks",
				"fieldname": "count_of_checks",
				"fieldtype": "Float",
				"width": 140
			}
		]
	elif filters.get('type') == "Monthly":
		return [

			
			{
				"label": "Customer",
				"fieldname": "cust_name",
				"fieldtype": "Link",
				"options": "Customer",
				"width": 180
			},
			{
				"label": "Date",
				"fieldname": "date",
				"fieldtype": "Date",
				"width": 120
			},
			{
				"label": "Store Id",
				"fieldname": "store_id",
				"fieldtype": "Link",
				"options": "Unit",
				"width": 120
			},
			{
				"label": "Zone",
				"fieldname": "zone",
				"fieldtype": "Link",
				"options": "Zone",
				"width": 100
			},
			{
				"label": "Total before tax and service",
				"fieldname": "totals_sub_total",
				"fieldtype": "Currency",
				"width": 150
			},
			{
				"label": "Discount Value",
				"fieldname": "totals_discount",
				"fieldtype": "Currency",
				"width": 120
			},
			{
				"label": "Service Charge",
				"fieldname": "totals_services",
				"fieldtype": "Currency",
				"width": 120
			},
			{
				"label": "Tax Value",
				"fieldname": "totals_taxes",
				"fieldtype": "Currency",
				"width": 120
			},
			{
				"label": "Total Check Value",
				"fieldname": "totals_net_total",
				"fieldtype": "Currency",
				"width": 140
			},
			{
				"label": "Count Of Checks",
				"fieldname": "count_of_checks",
				"fieldtype": "Float",
				"width": 140
			}
		]
	else:
		return [

			
			{
				"label": "Customer",
				"fieldname": "cust_name",
				"fieldtype": "Link",
				"options": "Customer",
				"width": 180
			},
			{
				"label": "Date",
				"fieldname": "date",
				"fieldtype": "Date",
				"width": 120
			},
			{
				"label": "Store Id",
				"fieldname": "store_id",
				"fieldtype": "Link",
				"options": "Unit",
				"width": 120
			},
			{
				"label": "Zone",
				"fieldname": "zone",
				"fieldtype": "Link",
				"options": "Zone",
				"width": 100
			},
			{
				"label": "Total before tax and service",
				"fieldname": "totals_sub_total",
				"fieldtype": "Currency",
				"width": 150
			},
			{
				"label": "Discount Value",
				"fieldname": "totals_discount",
				"fieldtype": "Currency",
				"width": 120
			},
			{
				"label": "Service Charge",
				"fieldname": "totals_services",
				"fieldtype": "Currency",
				"width": 120
			},
			{
				"label": "Tax Value",
				"fieldname": "totals_taxes",
				"fieldtype": "Currency",
				"width": 120
			},
			{
				"label": "Total Check Value",
				"fieldname": "totals_net_total",
				"fieldtype": "Currency",
				"width": 140
			},
			{
				"label": "Count Of Checks",
				"fieldname": "count_of_checks",
				"fieldtype": "Float",
				"width": 140
			}
		]
def get_data(filters, columns):
	item_price_qty_data = []
	item_price_qty_data = get_item_price_qty_data(filters)
	return item_price_qty_data


def get_item_price_qty_data(filters):
	conditions = ""
	conditions1 = ""
	if filters.get("from_date"):
		conditions1 += " and `tabRevenue Share Transaction`.date>=%(from_date)s"
	if filters.get("to_date"):
		conditions1 += " and `tabRevenue Share Transaction`.date<=%(to_date)s"
	if filters.get("customer"):
		conditions += " and `tabRevenue Share Transaction`.cust_name =%(customer)s"
	if filters.get("store_id"):
		conditions += " and `tabRevenue Share Transaction`.store_id =%(store_id)s"
	if filters.get("zone"):
		conditions += " and `tabRevenue Share Transaction`.zone =%(zone)s"
	fiscal_year = filters.get('fiscal_year')
	result = []
	if filters.get('type') == "Daily":
		item_result = frappe.db.sql("""
									SELECT
									`tabRevenue Share Transaction`.name as name,
									`tabRevenue Share Transaction`.cust_name as customer,
									`tabRevenue Share Transaction`.date as date,
									`tabRevenue Share Transaction`.zone as zone,
									`tabRevenue Share Transaction`.store_id as store_id,
									`tabRevenue Share Transaction`.count_of_checks as count_of_checks,
									`tabRevenue Share Transaction Details`.invc_id as invc_id,
									`tabRevenue Share Transaction Details`.invc_no as invc_no,
									`tabRevenue Share Transaction Details`.sub_total as sub_total,
									`tabRevenue Share Transaction Details`.discount as discount,
									`tabRevenue Share Transaction Details`.services as services,
									`tabRevenue Share Transaction Details`.taxes as taxes,
									`tabRevenue Share Transaction Details`.net_total as net_total
							 FROM
								 `tabRevenue Share Transaction` join `tabRevenue Share Transaction Details` on `tabRevenue Share Transaction`.name = `tabRevenue Share Transaction Details`.parent
							 WHERE
								 `tabRevenue Share Transaction`.docstatus = 1
								{conditions}
								{conditions1}
							""".format(conditions=conditions, conditions1=conditions1), filters, as_dict=1)


		if item_result:
			for item_dict in item_result:
				data = {
					'name': item_dict.name,
					'cust_name': item_dict.customer,
					'date': item_dict.date,
					'zone': item_dict.zone,
					'store_id': item_dict.store_id,
					'invc_id': item_dict.invc_id,
					'invc_no': item_dict.invc_no,
					'sub_total': item_dict.sub_total,
					'discount': item_dict.discount,
					'services': item_dict.services,
					'taxes': item_dict.taxes,
					'net_total': item_dict.net_total,
					'count_of_checks': item_dict.count_of_checks,
				}
				result.append(data)
			return result

	if filters.get('type') == "Monthly":
		item_result = frappe.db.sql("""
						select
						`tabRevenue Share Transaction`.name as name,
						`tabRevenue Share Transaction`.cust_name as customer,
						`tabRevenue Share Transaction`.date as date,
						`tabRevenue Share Transaction`.zone as zone,
						`tabRevenue Share Transaction`.store_id as store_id,
						`tabRevenue Share Transaction`.count_of_checks as count_of_checks,
						sum(`tabRevenue Share Transaction`.totals_sub_total) as totals_sub_total,
						sum(`tabRevenue Share Transaction`.totals_discount) as totals_discount,
						sum(`tabRevenue Share Transaction`.totals_services) as totals_services,
						sum(`tabRevenue Share Transaction`.totals_net_total) as totals_net_total,
						sum(`tabRevenue Share Transaction`.totals_taxes) as totals_taxes

							FROM
								`tabRevenue Share Transaction`
							WHERE
								`tabRevenue Share Transaction`.docstatus = 1
							{conditions}
							{conditions1}
							group by `tabRevenue Share Transaction`.cust_name
						""".format(conditions=conditions, conditions1=conditions1), filters, as_dict=1)

		if item_result:
			for item_dict in item_result:
				data = {
					'cust_name': item_dict.customer,
					'date': item_dict.date,
					'zone': item_dict.zone,
					'store_id': item_dict.store_id,
					'totals_sub_total': item_dict.totals_sub_total,
					'totals_discount': item_dict.totals_discount,
					'totals_services': item_dict.totals_services,
					'totals_taxes': item_dict.totals_taxes,
					'totals_net_total': item_dict.totals_net_total,
					'count_of_checks': item_dict.count_of_checks,
				}
				result.append(data)
			return result

	if filters.get('type') == "Yearly":
		item_result = frappe.db.sql("""
							select
							`tabRevenue Share Transaction`.name as name,
							`tabRevenue Share Transaction`.cust_name as customer,
							`tabRevenue Share Transaction`.date as date,
							`tabRevenue Share Transaction`.zone as zone,
							`tabRevenue Share Transaction`.store_id as store_id,
							`tabRevenue Share Transaction`.count_of_checks as count_of_checks,
							sum(`tabRevenue Share Transaction`.totals_sub_total) as totals_sub_total,
							sum(`tabRevenue Share Transaction`.totals_discount) as totals_discount,
							sum(`tabRevenue Share Transaction`.totals_services) as totals_services,
							sum(`tabRevenue Share Transaction`.totals_net_total) as totals_net_total,
							sum(`tabRevenue Share Transaction`.totals_taxes) as totals_taxes

							 FROM
								 `tabRevenue Share Transaction`
							 WHERE
								 `tabRevenue Share Transaction`.docstatus = 1
								 and `tabRevenue Share Transaction`.date < "{fiscal_year}-12-31"
								 and `tabRevenue Share Transaction`.date > "{fiscal_year}-01-01"
								{conditions}
								group by `tabRevenue Share Transaction`.cust_name
							""".format(conditions=conditions, fiscal_year=fiscal_year), filters, as_dict=1)

		if item_result:
			for item_dict in item_result:
				data = {
					'cust_name': item_dict.customer,
					'date': item_dict.date,
					'zone': item_dict.zone,
					'store_id': item_dict.store_id,
					'totals_sub_total': item_dict.totals_sub_total,
					'totals_discount': item_dict.totals_discount,
					'totals_services': item_dict.totals_services,
					'totals_taxes': item_dict.totals_taxes,
					'totals_net_total': item_dict.totals_net_total,
					'count_of_checks': item_dict.count_of_checks,
				}
				result.append(data)
			return result
