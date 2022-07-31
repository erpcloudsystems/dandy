// Copyright (c) 2022, ERP Cloud Systems and contributors
// For license information, please see license.txt

frappe.ui.form.on('Revenue Share Transaction', {
	// refresh: function(frm) {

	// }
});
frappe.ui.form.on("Revenue Share Transaction", {
	setup: function(frm) {
     frm.set_query("pms_lease_contract", function() {
	 return {
	  filters: [
	  ["PMS Lease Contract","party", "=", frm.doc.cust_name],
	  ["PMS Lease Contract","docstatus", "=", 1]
	  ]
	 };
	 });
	}
	});
