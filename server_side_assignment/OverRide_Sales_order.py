import frappe
from erpnext.selling.doctype.sales_order.sales_order import SalesOrder as OriginalSalesOrder

class CustomSalesOrder(OriginalSalesOrder):
    # This Function trigger when sales order page will be load
    def onload(self):
        frappe.msgprint("Override Sales Order onload")
        super(CustomSalesOrder, self).onload()
