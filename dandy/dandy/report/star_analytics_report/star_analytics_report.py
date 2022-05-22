# Copyright (c) 2022, ERP Cloud Systems and contributors
# For license information, please see license.txt

# import frappe

def execute(filters=None):
    columns, data = [], []
    columns = get_columns()
    data = get_data(filters, columns)
    return columns, data


def get_columns():
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
			"width": 180
		},
		{
			"label": "Store Id",
			"fieldname": "store_id",
			"fieldtype": "Link",
			"options": "Unit",
			"width": 180
		},
		{
			"label": "Check ID",
			"fieldname": "invc_id",
			"fieldtype": "Date",
			"width": 180
		},
		{
			"label": "Check NO",
			"fieldname": "invc_no",
			"fieldtype": "Date",
			"width": 180
		},
		{
			"label": "Total before tax and service",
			"fieldname": "sub_total",
			"fieldtype": "Float",
			"width": 180
		},
		{
			"label": "Discount Value",
			"fieldname": "discount",
			"fieldtype": "Float",
			"width": 180
		},
		{
			"label": "Service Charge",
			"fieldname": "services",
			"fieldtype": "Float",
			"width": 180
		},
		{
			"label": "Tax Value",
			"fieldname": "taxes",
			"fieldtype": "Float",
			"width": 180
		},
		{
			"label": "Total Check Value",
			"fieldname": "net_total",
			"fieldtype": "Float",
			"width": 180
		}
	]
def get_data(filters, columns):
    item_price_qty_data = []
    item_price_qty_data = get_item_price_qty_data(filters)
    return item_price_qty_data


def get_item_price_qty_data(filters):
    conditions = ""
    if filters.get("from_date"):
        conditions += " and `tabStar analytics`.date>=%(from_date)s"
    if filters.get("to_date"):
        conditions += " and `tabStar analytics`.date<=%(to_date)s"
    if filters.get("customer"):
        conditions += " and `tabStar analytics`.customer =%(customer)s"
    result = []
	item_results = frappe.db.sql("""
				SELECT
					`tabStar analytics`.cust_name as customer,
					`tabStar analytics`.date as date,
					`tabStar analytics`.store_id as store_id,
					`tabStar analytics Table`.invc_id as invc_id,
					`tabStar analytics Table`.invc_no as invc_no,
					`tabStar analytics Table`.sub_total as sub_total,
					`tabStar analytics Table`.discount as discount,
					`tabStar analytics Table`.services as services,
					`tabStar analytics Table`.taxes as taxes,
					`tabStar analytics Table`.net_total as net_total
				 FROM
								 `tabStar analytics` join `tabStar analytics Table` on `tabStar analytics`.name = `tabStar analytics Table`parent
							 WHERE
								 `tabtabStar analytics`.docstatus != 2
							 {conditions}
				 """.format(conditions=conditions), filters, as_dict=1)


if item_results:
	for item_dict in item_results:
		data = {
			'customer': item_dict.customer,
			'date': item_dict.date,
			'store_id': item_dict.store_id,
			'invc_id': item_dict.invc_id,
			'invc_no': item_dict.invc_no,
			'sub_total': item_dict.sub_total,
			'discount': item_dict.discount,
			'services': item_dict.services,
			'taxes': item_dict.taxes,
			'net_total': item_dict.net_total,

		}
		result.append(data)
return result