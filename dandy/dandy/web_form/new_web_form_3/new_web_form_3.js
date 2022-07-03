function Query(wh, fr, sl) {
    let m2 = 0;
    frappe.call({
        method: "Query",
        async: false,
        args: {
            select: sl,
            From: fr,
            WHERE: wh
        },
        callback: (r) => {
            m2 = r.message.toString();
        }
    });
    return m2;
}
	
frappe.ready(function() {
	frappe.web_form.after_load = () => {
		frappe.msgprint('Please fill all values carefully');
		
	},
	frappe.web_form.after_load = () => {
		frappe.msgprint('Please fill all values carefully 2');
		let wh = " name  = '" + cur_frm.web_form.cust_name + "' ";
		let sl = "`name`";
		let fr = "`tabCustomer`";
		let q = Query(wh, fr, sl);
		console.log(q);
	}
	// refresh(frm){
	// 	frappe.msgprint('Please fill all values carefully');
	// 	let wh = " name  = '" + cur_frm.doc.cust_name + "' ";
	// 	let sl = "`name`";
	// 	let fr = "`tabCustomer`";
	// 	let q = Query(wh, fr, sl);
	// 	console.log(q);
	// }
	// frappe.web_form.on('cust_name', (field, value) => {
	// 	value = frappe.web_form.get_value('cust_name');
	// 	frappe.web_form.set_value('customer_name', value);
	// });
	// cust_name:function(cur_frm){
	// let wh = " parent  = '" + cur_frm.doc.cust_name + "' ";
    // let sl = "`name`";
    // let fr = "`tabCustomer`";
    // let q = Query(wh, fr, sl);
	// console.log(q);
	// }
})
