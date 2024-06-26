## Server Side Assignment

server side asssignment

Overview

This project consists of multiple tasks aimed at enhancing and customizing an ERP system using the Frappe framework. The tasks include creating dashboards, generating reports, overriding Python classes, and developing various APIs for CRUD operations and user management. The detailed steps for each task are outlined below.

Installation
To get started with this project, follow these installation steps:

Set up a Frappe Bench environment:

Follow the official Frappe Bench Installation Guide to set up the Frappe Bench environment.
Create a new Frappe app:

bench new-app my_custom_app
Install the app:

bash
Copy code
bench get-app my_custom_app
bench --site [your-site-name] install-app my_custom_app
Start the bench:
bench start

Tasks
1. Create a Dashboard with Number Cards
Create a custom method to add number cards to the dashboard.
This method will involve defining the number cards' data source and layout in the dashboard.
2. Generate a Script Report
Create a script report with the following columns: customer name, sales order name, delivery date, item code, item name, and item quantity from sales order.
Follow Frappe's script report documentation for guidance.
3. Override Python Class
Identify the Python class to be overridden.
Use Frappe's customization hooks to override the class methods as needed.
4. Create an API for User Management
Develop an API to get a list of users.
Create an RPC API to create a new user.
5. CRUD Operations using Frappe RPC APIs
Create Frappe RPC APIs for CRUD (Create, Read, Update, Delete) operations of any doctype.
6. Create a New Doctype

Create a new doctype with fields: first name, last name, full name (data field), and a checkbox.
Implement logic such that if the checkbox is checked and both first name and last name are filled, the full name field concatenates the first and last name.
Usage
Using Postman for API Testing
Get Info
Endpoint: http://[your-site-name]/api/method/my_custom_app.api.get_info
Method: GET
Headers:
Authorization: token your_api_key
Response: Returns a list of all Info records.
Create Info
Endpoint: http://[your-site-name]/api/method/my_custom_app.api.create_info
Method: POST
Headers:
Authorization: token your_api_key
Content-Type: application/json
Body:

{
    "field_name": "value",
    "another_field": "another_value"
}
Response: Returns the name of the newly created Info record.
Update Info
Endpoint: http://[your-site-name]/api/method/my_custom_app.api.update_info
Method: POST
Headers:
Authorization: token your_api_key
Content-Type: application/json
Body:

{
    "name": "existing_info_name",
    "field_name": "updated_value",
    "another_field": "updated_value"
}
Response: Returns the updated Info record.
Delete Info
Endpoint: http://[your-site-name]/api/method/my_custom_app.api.delete_info
Headers:
Authorization: token your_api_key
Content-Type: application/json
Body:
json
Copy code
{
    "name": "existing_info_name"
}
Response: Returns a message confirming deletion.
Get Users
Endpoint: http://[your-site-name]/api/method/my_custom_app.api.get_user
Method: GET
Headers:
Authorization: token your_api_key
Response: Returns a list of all User records.
Create User
Endpoint: http://[your-site-name]/api/method/my_custom_app.api.create_user
Method: POST
Headers:
Authorization: token your_api_key
Content-Type: application/json
Body:

{
    "email": "user@example.com",
    "first_name": "First",
    "last_name": "Last",
    "send_welcome_email": 0
}
Response: Returns the name of the newly created User record.