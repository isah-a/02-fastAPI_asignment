# E-commerce API Documentation

This API provides endpoints for managing customers, products, and orders in an e-commerce system. It allows users to create, list, edit, and checkout orders, manage customers, and handle product inventory.

## Features

### 1. Manage Customers

- **Create Customer**: Create a new customer with a unique username and address.
- **List Customers**: Retrieve a list of all customers currently registered in the system.
- **Edit Customer**: Update the username and address of an existing customer.

### 2. Manage Products

- **Create Product**: Add a new product with a name, price, and available quantity.
- **List Products**: Retrieve a list of all available products in the inventory.
- **Edit Product**: Update the name and price of an existing product.

### 3. Manage Orders

- **Create Order**: Place a new order with a list of selected products and a customer ID.
- **List Orders**: View a list of all orders along with their details.
- **Checkout Order**: Change the status of a pending order to completed, indicating that it has been processed.

## Endpoints

### Customers

- `POST /customers/`: Create a new customer.
- `GET /customers/`: Retrieve a list of all customers.
- `PUT /customers/{customer_id}`: Update an existing customer's information.

### Products

- `POST /products/`: Add a new product to the inventory.
- `GET /products/`: Retrieve a list of all available products.
- `PUT /products/{product_id}`: Update the details of an existing product.

### Orders

- `POST /orders/`: Place a new order.
- `GET /orders/`: View a list of all orders.
- `PUT /orders/checkout/{order_id}`: Change the status of an order to completed.

## Usage

### Installation

1. Clone the repository: 
   ```bash
   git clone https://github.com/isah-a/02-fastAPI_asignment.git


```bash
pip install -r requirements.txt

```
```bash 
uvicorn main:app --reload
```