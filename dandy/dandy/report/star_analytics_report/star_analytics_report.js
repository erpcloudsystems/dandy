// Copyright (c) 2022, ERP Cloud Systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Star Analytics Report"] = {
	"filters": [


		{
			"fieldname": "type",
			"label": __("Report Type"),
			"fieldtype": "Select",
			"options":["","Daily","Monthly","Yearly"],
			"reqd": 1
		},
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"reqd": 1
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"reqd": 1
		},
		{
			"fieldname":"customer",
			"label": __("Customer"),
			"fieldtype": "Link",
			"options" : "Customer",
			"reqd": 0
		},
		{
			"fieldname":"store_id",
			"label": __("Unit"),
			"fieldtype": "Link",
			"options" : "Unit",
			"reqd": 0
		},
		{
			"fieldname":"zone",
			"label": __("Zone"),
			"fieldtype": "Link",
			"options" : "Zone",
			"reqd": 0
		}

	]
}
