// Copyright (c) 2022, ERP Cloud Systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["FootFall report"] = {
	"filters": [
		{
			"fieldname": "date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.defaults.get_user_default("year_start_date"),
			"reqd": 1
		},
		{
			"fieldname":"date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.defaults.get_user_default("year_end_date"),
			"reqd": 1
		},
		{
			"fieldname": "footfall_location",
			"label": __("Footfall Location"),
			"fieldtype": "Link",
			"options" : "Footfall Location",
			"reqd": 0
		}
]
};
