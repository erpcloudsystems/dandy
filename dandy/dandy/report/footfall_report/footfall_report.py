# Copyright (c) 2013, erpcloud.systems and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns, data = [], []
	columns = get_columns(filters)
	data = get_data(filters, columns)
	return columns, data


def get_columns(filters):
	if filters.get('shift') == "Morning Shift":
		return [
			
			{
				"label": _("FootFall Location"),
				"fieldname": "footfall_location",
				"fieldtype": "Link",
				"options": "FootFall Location",
				"width": 150
			},
			{
				"label": _("0 To 10"),
				"fieldname": "m_0_to_10",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("10 To 11"),
				"fieldname": "m_10_to_11",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("11 To 12"),
				"fieldname": "m_11_to_12",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("12 To 1"),
				"fieldname": "m_12_to_1",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _(" 1 To 2"),
				"fieldname": "m_1_to_2",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("2 To 3"),
				"fieldname": "m_2_to_3",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("3 To 4"),
				"fieldname": "m_3_to_4",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("4 To 5"),
				"fieldname": "m_4_to_5",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("Total"),
				"fieldname": "total",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("Percentage (%)"),
				"fieldname": "percentage",
				"fieldtype": "percent",
				"width": 120
			}
		]
	elif filters.get('shift') == "Night Shift":
		return [
			
			{
				"label": _("FootFall Location"),
				"fieldname": "footfall_location",
				"fieldtype": "Link",
				"options": "FootFall Location",
				"width": 150
			},
			{
				"label": _("5 To 6"),
				"fieldname": "n_5_to_6",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("6 To 7"),
				"fieldname": "n_6_to_7",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("7 To 8"),
				"fieldname": "n_7_to_8",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("8 To 9"),
				"fieldname": "n_8_to_9",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("9 To 10"),
				"fieldname": "n_9_to_10",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("10 To 11"),
				"fieldname": "n_10_to_11",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("11 To 12"),
				"fieldname": "n_11_to_12",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("12 To 1"),
				"fieldname": "n_12_to_1",
				"fieldtype": "Int",
				"width": 80
			}
			,
			{
				"label": _("Total"),
				"fieldname": "total",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("Percentage (%)"),
				"fieldname": "percentage",
				"fieldtype": "percent",
				"width": 120
			}
		]
	else:
		return [
			
			{
				"label": _("FootFall Location"),
				"fieldname": "footfall_location",
				"fieldtype": "Link",
				"options": "FootFall Location",
				"width": 150
			},
			{
				"label": _("0 To 10"),
				"fieldname": "m_0_to_10",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("10 To 11"),
				"fieldname": "m_10_to_11",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("11 To 12"),
				"fieldname": "m_11_to_12",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("12 To 1"),
				"fieldname": "m_12_to_1",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _(" 1 To 2"),
				"fieldname": "m_1_to_2",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("2 To 3"),
				"fieldname": "m_2_to_3",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("3 To 4"),
				"fieldname": "m_3_to_4",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("4 To 5"),
				"fieldname": "m_4_to_5",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("5 To 6"),
				"fieldname": "n_5_to_6",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("6 To 7"),
				"fieldname": "n_6_to_7",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("7 To 8"),
				"fieldname": "n_7_to_8",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("8 To 9"),
				"fieldname": "n_8_to_9",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("9 To 10"),
				"fieldname": "n_9_to_10",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("10 To 11"),
				"fieldname": "n_10_to_11",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("11 To 12"),
				"fieldname": "n_11_to_12",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("12 To 1"),
				"fieldname": "n_12_to_1",
				"fieldtype": "Int",
				"width": 80
			}
			,
			{
				"label": _("Total"),
				"fieldname": "total",
				"fieldtype": "Int",
				"width": 80
			},
			{
				"label": _("Percentage (%)"),
				"fieldname": "percentage",
				"fieldtype": "percent",
				"width": 120
			}
		]

def get_data(filters, columns):
	item_price_qty_data = []
	item_price_qty_data = get_item_price_qty_data(filters)
	return item_price_qty_data


def get_item_price_qty_data(filters):
	conditions = ""
	if filters.get("from_date"):
		conditions += " and `tabFootfall`.date>=%(from_date)s"
	if filters.get("to_date"):
		conditions += " and `tabFootfall`.date<=%(to_date)s"
	if filters.get("footfall_location"):
		conditions += " and `tabShift`.footfall_location =%(footfall_location)s"
	result = []
	if filters.get('shift') == "Morning Shift":
		item_results = frappe.db.sql("""
					select distinct
							`tabFootfall`.name as name,
							ifnull(`tabFootfall`.total_of_day, 1) as total_of_day,
							`tabShift`.footfall_location as footfall_location,
							ifnull(sum(`tabShift`.act_0_to_10), 0) as m_0_to_10,
							ifnull(sum(`tabShift`.act_10_to_11), 0) as m_10_to_11,
							ifnull(sum(`tabShift`.act_11_to_12), 0) as m_11_to_12,
							ifnull(sum(`tabShift`.act_12_to_1), 0) as m_12_to_1,
							ifnull(sum(`tabShift`.act_1_to_2), 0) as m_1_to_2,
							ifnull(sum(`tabShift`.act_2_to_3), 0) as m_2_to_3,
							ifnull(sum(`tabShift`.act_3_to_4), 0) as m_3_to_4,
							ifnull(sum(`tabShift`.act_4_to_5), 0) as m_4_to_5

					from `tabFootfall` join `tabShift` on `tabShift`.parent = `tabFootfall`.name
					where `tabFootfall`.docstatus = 1
					{conditions}
					group by `tabShift`.footfall_location
					""".format(conditions=conditions), filters, as_dict=1)

		if item_results:
			for item_dict in item_results:
				data = {
					'footfall_location': item_dict.footfall_location,
					'm_0_to_10': item_dict.m_0_to_10,
					'm_10_to_11': item_dict.m_10_to_11,
					'm_11_to_12': item_dict.m_11_to_12,
					'm_12_to_1': item_dict.m_12_to_1,
					'm_1_to_2': item_dict.m_1_to_2,
					'm_2_to_3': item_dict.m_2_to_3,
					'm_3_to_4': item_dict.m_3_to_4,
					'm_4_to_5': item_dict.m_4_to_5,
					'total': item_dict.m_4_to_5 + item_dict.m_3_to_4 + item_dict.m_2_to_3 + item_dict.m_1_to_2 + item_dict.m_12_to_1 + item_dict.m_11_to_12 + item_dict.m_10_to_11 + item_dict.m_0_to_10,
					'percentage': round((item_dict.m_4_to_5 + item_dict.m_3_to_4 + item_dict.m_2_to_3 + item_dict.m_1_to_2 + item_dict.m_12_to_1 + item_dict.m_11_to_12 + item_dict.m_10_to_11 + item_dict.m_0_to_10) / item_dict.total_of_day * 100)
				}
				result.append(data)
			return result

	elif filters.get('shift') == "Night Shift":
		item_results = frappe.db.sql("""
						select distinct
								`tabFootfall`.name as name,
								ifnull(`tabFootfall`.total_of_day, 1) as total_of_day,
								`tabShift`.footfall_location as footfall_location,
								ifnull(sum(`tabShift`.act_n_5_to_6), 0) as n_5_to_6,
								ifnull(sum(`tabShift`.act_n_6_to_7), 0) as n_6_to_7,
								ifnull(sum(`tabShift`.act_n_7_to_8), 0) as n_7_to_8,
								ifnull(sum(`tabShift`.act_n_8_to_9), 0) as n_8_to_9,
								ifnull(sum(`tabShift`.act_n_9_to_10), 0) as n_9_to_10,
								ifnull(sum(`tabShift`.act_n_10_to_11), 0) as n_10_to_11,
								ifnull(sum(`tabShift`.act_n_11_to_12), 0) as n_11_to_12,
								ifnull(sum(`tabShift`.act_n_12_to_1), 0) as n_12_to_1

						from `tabFootfall` join `tabShift` on `tabShift`.parent = `tabFootfall`.name
						where `tabFootfall`.docstatus = 1
						{conditions}
						group by `tabShift`.footfall_location
					""".format(conditions=conditions), filters, as_dict=1)

		if item_results:
			for item_dict in item_results:

				data = {
					'footfall_location': item_dict.footfall_location,
					'n_5_to_6': item_dict.n_5_to_6,
					'n_6_to_7': item_dict.n_6_to_7,
					'n_7_to_8': item_dict.n_7_to_8,
					'n_8_to_9': item_dict.n_8_to_9,
					'n_9_to_10': item_dict.n_9_to_10,
					'n_10_to_11': item_dict.n_10_to_11,
					'n_11_to_12': item_dict.n_11_to_12,
					'n_12_to_1': item_dict.n_12_to_1,
					'total': item_dict.n_5_to_6 + item_dict.n_6_to_7 + item_dict.n_7_to_8 + item_dict.n_8_to_9 + item_dict.n_9_to_10 + item_dict.n_10_to_11 + item_dict.n_11_to_12 + item_dict.n_12_to_1,
					'percentage': round((item_dict.n_5_to_6 + item_dict.n_6_to_7 + item_dict.n_7_to_8 + item_dict.n_8_to_9 + item_dict.n_9_to_10 + item_dict.n_10_to_11 + item_dict.n_11_to_12 + item_dict.n_12_to_1) / item_dict.total_of_day * 100)

				}
				result.append(data)
			return result
	else:
		item_results = frappe.db.sql("""
					select distinct
							`tabFootfall`.name as name,
							ifnull(`tabFootfall`.total_of_day , 1)as total_of_day,
							`tabShift`.footfall_location as footfall_location,
							ifnull(sum(`tabShift`.act_0_to_10), 0) as m_0_to_10,
							ifnull(sum(`tabShift`.act_10_to_11), 0) as m_10_to_11,
							ifnull(sum(`tabShift`.act_11_to_12), 0) as m_11_to_12,
							ifnull(sum(`tabShift`.act_12_to_1), 0) as m_12_to_1,
							ifnull(sum(`tabShift`.act_1_to_2), 0) as m_1_to_2,
							ifnull(sum(`tabShift`.act_2_to_3), 0) as m_2_to_3,
							ifnull(sum(`tabShift`.act_3_to_4), 0) as m_3_to_4,
							ifnull(sum(`tabShift`.act_4_to_5), 0) as m_4_to_5,
							ifnull(sum(`tabShift`.act_n_5_to_6), 0) as n_5_to_6,
							ifnull(sum(`tabShift`.act_n_6_to_7), 0) as n_6_to_7,
							ifnull(sum(`tabShift`.act_n_7_to_8), 0) as n_7_to_8,
							ifnull(sum(`tabShift`.act_n_8_to_9), 0) as n_8_to_9,
							ifnull(sum(`tabShift`.act_n_9_to_10), 0) as n_9_to_10,
							ifnull(sum(`tabShift`.act_n_10_to_11), 0) as n_10_to_11,
							ifnull(sum(`tabShift`.act_n_11_to_12), 0) as n_11_to_12,
							ifnull(sum(`tabShift`.act_n_12_to_1), 0) as n_12_to_1
							from `tabFootfall` join `tabShift` on `tabShift`.parent = `tabFootfall`.name
						where `tabFootfall`.docstatus = 1
							{conditions}
							group by `tabShift`.footfall_location
					""".format(conditions=conditions), filters, as_dict=1)

		if item_results:
			for item_dict in item_results:
				data = {
					'footfall_location': item_dict.footfall_location,
					'm_0_to_10': item_dict.m_0_to_10,
					'm_10_to_11': item_dict.m_10_to_11,
					'm_11_to_12': item_dict.m_11_to_12,
					'm_12_to_1': item_dict.m_12_to_1,
					'm_1_to_2': item_dict.m_1_to_2,
					'm_2_to_3': item_dict.m_2_to_3,
					'm_3_to_4': item_dict.m_3_to_4,
					'm_4_to_5': item_dict.m_4_to_5,
					'n_5_to_6': item_dict.n_5_to_6,
					'n_6_to_7': item_dict.n_6_to_7,
					'n_7_to_8': item_dict.n_7_to_8,
					'n_8_to_9': item_dict.n_8_to_9,
					'n_9_to_10': item_dict.n_9_to_10,
					'n_10_to_11': item_dict.n_10_to_11,
					'n_11_to_12': item_dict.n_11_to_12,
					'n_12_to_1': item_dict.n_12_to_1,
					'total': item_dict.m_4_to_5 + item_dict.m_3_to_4 + item_dict.m_2_to_3 + item_dict.m_1_to_2 + item_dict.m_12_to_1 + item_dict.m_11_to_12 + item_dict.m_10_to_11 + item_dict.m_0_to_10 + item_dict.n_5_to_6 + item_dict.n_6_to_7 + item_dict.n_7_to_8 + item_dict.n_8_to_9 + item_dict.n_9_to_10 + item_dict.n_10_to_11 + item_dict.n_11_to_12 + item_dict.n_12_to_1,
					'percentage': round((item_dict.m_4_to_5 + item_dict.m_3_to_4 + item_dict.m_2_to_3 + item_dict.m_1_to_2 + item_dict.m_12_to_1 + item_dict.m_11_to_12 + item_dict.m_10_to_11 + item_dict.m_0_to_10 + item_dict.n_5_to_6 + item_dict.n_6_to_7 + item_dict.n_7_to_8 + item_dict.n_8_to_9 + item_dict.n_9_to_10 + item_dict.n_10_to_11 + item_dict.n_11_to_12 + item_dict.n_12_to_1) / item_dict.total_of_day * 100)

				}
				result.append(data)
			return result
