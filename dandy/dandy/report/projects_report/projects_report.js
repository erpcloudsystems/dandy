// Copyright (c) 2022, ERP Cloud Systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Projects Report"] = {
	"filters": [
        {
			"fieldname":"project",
			"label": __("Project"),
			"fieldtype": "Link",
			"options":  "Project",
		},
		{
			"fieldname":"unit",
			"label": __("Unit"),
			"fieldtype": "Link",
			"options":  "Unit",
		},
		{
			"fieldname":"project_manager",
			"label": __("Project Manager"),
			"fieldtype": "Link",
			"options":  "User",
		},
		{
			"fieldname":"project_type",
			"label": __("Project Type"),
			"fieldtype": "Link",
			"options":  "Project Type",
		},
		{
			"fieldname":"status",
			"label": __("Status"),
			"fieldtype": "Select",
			"options":  ["Open", "Completed"],
		},
	]
};