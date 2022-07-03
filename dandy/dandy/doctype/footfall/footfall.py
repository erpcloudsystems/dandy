# Copyright (c) 2022, ERP Cloud Systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Footfall(Document):
	@frappe.whitelist()
	def validate(self):
		

		self.night_shift_total = 0
		self.morning_shift_total = 0
		
		
		for x in self.shift:
			act_0_to_10 = x.m_0_to_10
			x.act_0_to_10 = act_0_to_10
			
			act_10_to_11 = (x.m_10_to_11 - x.m_0_to_10) if x.m_10_to_11 > 0 else 0
			x.act_10_to_11 = act_10_to_11
			
			act_11_to_12 = (x.m_11_to_12 - x.m_10_to_11) if x.m_11_to_12 > 0 else 0
			x.act_11_to_12 = act_11_to_12
			
			act_12_to_1 = (x.m_12_to_1 - x.m_11_to_12) if x.m_12_to_1 > 0 else 0
			x.act_12_to_1 = act_12_to_1
			
			act_1_to_2 = (x.m_1_to_2 - x.m_12_to_1) if x.m_1_to_2 > 0 else 0
			x.act_1_to_2 = act_1_to_2
			
			act_2_to_3 = (x.m_2_to_3 - x.m_1_to_2) if x.m_2_to_3 > 0 else 0
			x.act_2_to_3 = act_2_to_3
			
			act_3_to_4 = (x.m_3_to_4 - x.m_2_to_3) if x.m_3_to_4 > 0 else 0
			x.act_3_to_4 = act_3_to_4
			
			act_4_to_5 = (x.m_4_to_5 - x.m_3_to_4) if x.m_4_to_5 > 0 else 0
			x.act_4_to_5 = act_4_to_5
			
			act_n_5_to_6 = (x.n_5_to_6 - x.m_4_to_5) if x.n_5_to_6 > 0 else 0
			x.act_n_5_to_6 = act_n_5_to_6
			
			act_n_6_to_7 = (x.n_6_to_7 - x.n_5_to_6) if x.n_6_to_7 > 0 else 0
			x.act_n_6_to_7 = act_n_6_to_7
			
			act_n_7_to_8 = (x.n_7_to_8 - x.n_6_to_7) if x.n_7_to_8 > 0 else 0
			x.act_n_7_to_8 = act_n_7_to_8
			
			act_n_8_to_9 = (x.n_8_to_9 - x.n_7_to_8) if x.n_8_to_9 > 0 else 0
			x.act_n_8_to_9 = act_n_8_to_9
			
			act_n_9_to_10 = (x.n_9_to_10 - x.n_8_to_9) if x.n_9_to_10 > 0 else 0
			x.act_n_9_to_10 = act_n_9_to_10
			
			act_n_10_to_11 = (x.n_10_to_11 - x.n_9_to_10) if x.n_10_to_11 > 0 else 0
			x.act_n_10_to_11 = act_n_10_to_11
			
			act_n_11_to_12 = (x.n_11_to_12 - x.n_10_to_11) if x.n_11_to_12 > 0 else 0
			x.act_n_11_to_12 = act_n_11_to_12
			
			act_n_12_to_1 = (x.n_12_to_1 - x.n_11_to_12) if x.n_12_to_1 > 0 else 0
			x.act_n_12_to_1 = act_n_12_to_1
			
			
			x.morning_shift_total = x.act_4_to_5 + x.act_3_to_4 + x.act_2_to_3 + x.act_1_to_2 + x.act_12_to_1 + x.act_11_to_12 + x.act_10_to_11 + x.act_0_to_10
			x.night_shift_total = x.act_n_5_to_6 + x.act_n_6_to_7 + x.act_n_7_to_8 + x.act_n_8_to_9 + x.act_n_9_to_10 + x.act_n_10_to_11 + x.act_n_11_to_12 + x.act_n_12_to_1
			x.loc_total = x.morning_shift_total + x.night_shift_total
		for z in self.shift:	
			self.night_shift_total += z.night_shift_total
			self.morning_shift_total += z.morning_shift_total
		self.total_of_day = self.night_shift_total + self.morning_shift_total
		for y in self.shift:
			y.percentage = (y.loc_total / self.total_of_day) * 100
		if self.validate_from_count == 1:
			if act_0_to_10 < 0:
							frappe.throw(('Please Set Correct Value'))
			if act_10_to_11 < 0:
							frappe.throw(('Please Set Correct Value'))
			if act_11_to_12 < 0:
							frappe.throw(('Please Set Correct Value'))
			if act_12_to_1 < 0:
							frappe.throw(('Please Set Correct Value'))
			if act_1_to_2 < 0:
							frappe.throw(('Please Set Correct Value'))
			if act_2_to_3 < 0:
							frappe.throw(('Please Set Correct Value'))
			if act_3_to_4 < 0:
							frappe.throw(('Please Set Correct Value'))
			if act_4_to_5 < 0:
							frappe.throw(('Please Set Correct Value'))
			if act_n_5_to_6 < 0:
							frappe.throw(('Please Set Correct Value'))
			if act_n_6_to_7 < 0:
							frappe.throw(('Please Set Correct Value'))
			if act_n_7_to_8 < 0:
							frappe.throw(('Please Set Correct Value'))
			if act_n_8_to_9 < 0:
							frappe.throw(('Please Set Correct Value'))
			if act_n_9_to_10 < 0:
							frappe.throw(('Please Set Correct Value'))
			if act_n_10_to_11 < 0:
							frappe.throw(('Please Set Correct Value'))
			if act_n_11_to_12 < 0:
							frappe.throw(('Please Set Correct Value'))