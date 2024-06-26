import frappe

@frappe.whitelist()
def getTotalSalesOrder():
    # this function return all sales order count that are submitted
    return frappe.db.count('Sales Order',{'docstatus':1})

@frappe.whitelist()
def getTotalQuantity():
    # this function sum all quanity via sql query
    return frappe.db.sql("""SELECT SUM(qty)
        FROM `tabSales Order Item`
        WHERE parent IN (SELECT name FROM `tabSales Order` WHERE docstatus = 1)""")[0][0]
