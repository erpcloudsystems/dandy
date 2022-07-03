# Copyright (c) 2022, ERP Cloud Systems and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	columns, data = [], []
	columns = get_columns(filters)
	data = get_data(filters, columns)
	return columns, data


def get_columns(filters):
	if filters.get('type') == "Daily":
		return [

			{
				"label": "Star Analystics",
				"fieldname": "name",
				"fieldtype": "Link",
				"options": "Star analytics",
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
			}
		]

def get_data(filters, columns):
	item_price_qty_data = []
	item_price_qty_data = get_item_price_qty_data(filters)
	return item_price_qty_data


def get_item_price_qty_data(filters):
	conditions = ""
	if filters.get("from_date"):
		conditions += " and `tabStar Analytics`.date>=%(from_date)s"
	if filters.get("to_date"):
		conditions += " and `tabStar Analytics`.date<=%(to_date)s"
	if filters.get("customer"):
		conditions += " and `tabStar Analytics`.cust_name =%(customer)s"
	if filters.get("store_id"):
		conditions += " and `tabStar Analytics`.store_id =%(store_id)s"
	if filters.get("zone"):
		conditions += " and `tabStar Analytics`.zone =%(zone)s"
	results = []
	if filters.get('type') == "Daily":
		item_result = frappe.db.sql("""
							SELECT
							`tabStar Analytics`.name as name,
							`tabStar Analytics`.cust_name as customer,
							`tabStar Analytics`.date as date,
							`tabStar Analytics`.zone as zone,
							`tabStar Analytics`.store_id as store_id,
							`tabStar Analytics Table`.invc_id as invc_id,
							`tabStar Analytics Table`.invc_no as invc_no,
							`tabStar Analytics Table`.sub_total as sub_total,
							`tabStar Analytics Table`.discount as discount,
							`tabStar Analytics Table`.services as services,
							`tabStar Analytics Table`.taxes as taxes,
							`tabStar Analytics Table`.net_total as net_total
							 FROM
								 `tabStar Analytics` join `tabStar Analytics Table` on `tabStar Analytics`.name = `tabStar Analytics Table`.parent
							 WHERE
								 `tabStar Analytics`.docstatus = 1
								{conditions}
							""".format(conditions=conditions), filters, as_dict=1)


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
					}
			results.append(data)
		return results
	
	if filters.get('type') == "Monthly":
		item_result2 = frappe.db.sql("""
									select
									`tabStar Analytics`.cust_name as customer,
									`tabStar Analytics`.date as date,
									`tabStar Analytics`.zone as zone,
									`tabStar Analytics`.store_id as store_id,
									sum(`tabStar Analytics`.totals_sub_total) as totals_sub_total,
									sum(`tabStar Analytics`.totals_discount) as totals_discount,
									sum(`tabStar Analytics`.totals_services) as totals_services,
									sum(`tabStar Analytics`.totals_net_total) as totals_net_total,
									sum(`tabStar Analytics`.totals_taxes) as totals_taxes

									 FROM
										 `tabStar Analytics`
									 WHERE
										 `tabStar Analytics`.docstatus = 1
										{conditions}
									""".format(conditions=conditions), filters, as_dict=1)

		if item_result2:
			for item_dict in item_result2:
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
				}
			results.append(data)
		return results
	
	if filters.get('type') == "Yearly":
		item_result3 = frappe.db.sql("""
							select
							`tabStar Analytics`.cust_name as customer,
							`tabStar Analytics`.date as date,
							`tabStar Analytics`.zone as zone,
							`tabStar Analytics`.store_id as store_id,
							sum(`tabStar Analytics`.totals_sub_total) as totals_sub_total,
							sum(`tabStar Analytics`.totals_discount) as totals_discount,
							sum(`tabStar Analytics`.totals_services) as totals_services,
							sum(`tabStar Analytics`.totals_net_total) as totals_net_total,
							sum(`tabStar Analytics`.totals_taxes) as totals_taxes

							 FROM
								 `tabStar Analytics`
							 WHERE
								 `tabStar Analytics`.docstatus = 1
								{conditions}
							""".format(conditions=conditions), filters, as_dict=1)

		if item_result3:
			for item_dict in item_result3:
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
				}
			results.append(data)
		return results
