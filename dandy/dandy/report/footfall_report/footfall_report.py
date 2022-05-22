# Copyright (c) 2013, erpcloud.systems and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _


def execute(filters=None):
    columns, data = [], []
    columns = get_columns()
    data = get_data(filters, columns)
    return columns, data


def get_columns():
    return [
        {
            "label": _("FootFall Location"),
            "fieldname": "footfall_location",
            "fieldtype": "Link",
            "options": "FootFall Location",
            "width": 180
        },
        {
            "label": _("0 To 10"),
            "fieldname": "m_0_to_10",
            "fieldtype": "Int",
            "width": 180
        },
		{
			"label": _("10 To 11"),
			"fieldname": "count_of_press_release",
			"fieldtype": "Int",
			"width": 180
		},
		{
			"label": _("11 To 12"),
			"fieldname": "count_of_press_release",
			"fieldtype": "Int",
			"width": 180
		},
		{
			"label": _("12 To 1"),
			"fieldname": "count_of_press_release",
			"fieldtype": "Int",
			"width": 180
		},
		{
            "label": _(" 1 To 2"),
            "fieldname": "count_of_press_release",
            "fieldtype": "Int",
            "width": 180
        },
		{
			"label": _("2 To 3"),
			"fieldname": "count_of_press_release",
			"fieldtype": "Int",
			"width": 180
		},
		{
			"label": _("3 To 4"),
			"fieldname": "count_of_press_release",
			"fieldtype": "Int",
			"width": 180
		},
		{
			"label": _("4 To 5"),
			"fieldname": "count_of_press_release",
			"fieldtype": "Int",
			"width": 180
		},
		{
			"label": _("5 To 6"),
			"fieldname": "count_of_press_release",
			"fieldtype": "Int",
			"width": 180
		},
		{
			"label": _("6 To 7"),
			"fieldname": "count_of_press_release",
			"fieldtype": "Int",
			"width": 180
		},
		{
			"label": _("7 To 8"),
			"fieldname": "count_of_press_release",
			"fieldtype": "Int",
			"width": 180
		},
		{
			"label": _("8 To 9"),
			"fieldname": "count_of_press_release",
			"fieldtype": "Int",
			"width": 180
		},
		{
			"label": _("9 To 10"),
			"fieldname": "count_of_press_release",
			"fieldtype": "Int",
			"width": 180
		},
		{
			"label": _("10 To 11"),
			"fieldname": "count_of_press_release",
			"fieldtype": "Int",
			"width": 180
		},
		{
			"label": _("11 To 12"),
			"fieldname": "count_of_press_release",
			"fieldtype": "Int",
			"width": 180
		},
		{
			"label": _("12 To 1"),
			"fieldname": "count_of_press_release",
			"fieldtype": "Int",
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
        conditions += " and `tabFootfall`.date>=%(date)s"
    if filters.get("to_date"):
        conditions += " and `tabFootfall`.date<=%(date)s"
    if filters.get("footfall_location"):
        conditions += " and `tabatreem`.footfall_location =%(footfall_location)s"
    item_results = frappe.db.sql("""
				select distinct
						`tabatreem`.footfall_location as footfall_location,
						`tabatreem`.sum(m_0_to_10) as m_0_to_10

				from `tabatreem` join `tabFootfall` on `tabatreem`.parent = `tabFootfall`.name 
				and `tabFootfall`.shift = "Morning Shift"
				and `tabFootfall`.docstatus = 1
				{conditions}
				""".format(conditions=conditions), filters, as_dict=1)

    result = []
    if item_results:
        for item_dict in item_results:
            data = {
                'footfall_location': item_dict.footfall_location,
                'm_0_to_10': item_dict.m_0_to_10
            }
            result.append(data)

    return result
