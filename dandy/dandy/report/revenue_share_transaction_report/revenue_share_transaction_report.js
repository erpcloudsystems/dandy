// Copyright (c) 2022, ERP Cloud Systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Revenue Share Transaction Report"] = {
	"filters": [


		{
			"fieldname": "type",
			"label": __("Report Type"),
			"fieldtype": "Select",
			"options":["Daily","Monthly","Yearly"],
			"default": ["Yearly"],
			"reqd": 1,
			on_change: function() {
				let type = frappe.query_report.get_filter_value('type');
				frappe.query_report.toggle_filter_display('from_date', type === 'Yearly');
				frappe.query_report.toggle_filter_display('to_date', type === 'Yearly');
				frappe.query_report.toggle_filter_display('fiscal_year', (type === 'Daily' || type ==='Monthly'));
				frappe.query_report.set_filter_value('from_date', '');
				frappe.query_report.set_filter_value('to_date', ''); 
				frappe.query_report.set_filter_value('fiscal_year', '');
				frappe.query_report.refresh();
				
			
			}
		},
		{
			"fieldname": "fiscal_year",
			"label": __("Fiscal Year"),
			"fieldtype": "Link",
			"options" : "Fiscal Year",
			"reqd": 0,
			"default": frappe.defaults.get_user_default("fiscal_year")
			
		},
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"reqd": 0
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"reqd": 0
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