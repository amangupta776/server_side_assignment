# Copyright (c) 2024, Aman and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Info(Document):
	#This Function is checking First , last name is present and check box is checked or not if all three are ok then full name is autofill 
	def before_save(self):
		if self.first_name and self.last_name and self.check:
			self.full_name=f"{self.first_name} {self.last_name}"
		else:
			self.full_name=f""

		
