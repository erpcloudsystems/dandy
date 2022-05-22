# Copyright (c) 2013, erpcloud.systems and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns, data = [], []
	columns=get_columns()
	data=get_data(filters,columns)
	return columns, data

def get_columns():
	return [
		{
			"label": _("Project"),
			"fieldname": "project",
			"fieldtype": "Link",
			"options": "Project",
			"width": 130
		},
		{
			"label": _("Project Name"),
			"fieldname": "project_name",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Status"),
			"fieldname": "status",
			"fieldtype": "Data",
			"width": 110
		},
		{
			"label": _("% Completed"),
			"fieldname": "percent_complete",
			"fieldtype": "Percent",
			"width": 110
		},
		{
			"label": _("Project Type"),
			"fieldname": "project_type",
			"fieldtype": "Data",
			"width": 110
		},
		{
			"label": _("Supplier"),
			"fieldname": "supplier",
			"fieldtype": "Data",
			"width": 130
		},
		{
			"label": _("Project Manager"),
			"fieldname": "project_manager_name",
			"fieldtype": "Data",
			"width": 140
		},
		{
			"label": _("Expected Start Date"),
			"fieldname": "expected_start_date",
			"fieldtype": "Date",
			"width": 160
		},
		{
			"label": _("Expected End Date"),
			"fieldname": "expected_end_date",
			"fieldtype": "Date",
			"width": 160
		},
		{
			"label": _("Unit"),
			"fieldname": "unit",
			"fieldtype": "Data",
			"width": 140
		},
		{
			"label": _("Customer"),
			"fieldname": "customer",
			"fieldtype": "Data",
			"width": 130
		},
		{
			"label": _("Estimated Cost"),
			"fieldname": "estimated_costing",
			"fieldtype": "Currency",
			"width": 130
		},
		{
			"label": _("Actual Cost"),
			"fieldname": "actual_cost",
			"fieldtype": "Currency",
			"width": 130
		}
	]

def get_data(filters, columns):
	item_price_qty_data = []
	item_price_qty_data = get_item_price_qty_data(filters)
	return item_price_qty_data

def get_item_price_qty_data(filters):
	conditions = ""
	if filters.get("unit"):
		conditions += " and a.unit=%(unit)s"
	if filters.get("project"):
		conditions += " and a.name=%(project)s"
	if filters.get("project_manager"):
		conditions += " and a.project_manager=%(project_manager)s"
	if filters.get("project_type"):
		conditions += " and a.project_type=%(project_type)s"
	if filters.get("status"):
		conditions += " and a.status=%(status)s"

	item_results = frappe.db.sql("""
				select
					a.name as project,
					a.project_name as project_name,
					a.status as status,
					a.percent_complete as percent_complete,
					a.project_type as project_type,
					a.supplier as supplier,
					a.project_manager_name as project_manager_name,
					a.expected_start_date as expected_start_date,
					a.expected_end_date as expected_end_date,
					a.unit as unit,
					a.customer as customer,
					a.estimated_costing as estimated_costing,
					a.total_consumed_material_cost as total_consumed_material_cost,
					a.total_purchase_cost as total_purchase_cost				
				from `tabProject` a 
				where
					a.status in ("Open", "Completed")
					{conditions}
				""".format(conditions=conditions), filters, as_dict=1)

	result = []
	if item_results:
		for item_dict in item_results:
			data = {
				'project': item_dict.project,
				'project_name': item_dict.project_name,
				'status': item_dict.status,
				'percent_complete': item_dict.percent_complete,
				'project_type': item_dict.project_type,
				'supplier': item_dict.supplier,
				'project_manager_name': item_dict.project_manager_name,
				'expected_start_date': item_dict.expected_start_date,
				'expected_end_date': item_dict.expected_end_date,
				'unit': item_dict.unit,
				'customer': item_dict.customer,
				'estimated_costing': item_dict.estimated_costing,
				'actual_cost': item_dict.total_consumed_material_cost + item_dict.total_purchase_cost,
			}
			result.append(data)

	return result

