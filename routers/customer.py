from fastapi import APIRouter, HTTPException, Depends

from schema.customer import Customer, CustomerCreate, customers
from services.customer import check_username

customer_router = APIRouter()

# Create customer 
# List customer
# edit customer


###################### Added the dependecy to check if a customer already exists####################
# create customer
@customer_router.post('/', status_code=201, dependencies=[Depends(check_username.check_unique_username)]) 
def create_customer(payload: CustomerCreate):
    customer_id = len(customers) + 1
    new_customer = Customer(
        id=customer_id, 
        username=payload.username, 
        address=payload.address
    )
    customers.append(new_customer)
    return {'message': 'customer created successfully', 'data': new_customer}

@customer_router.get('/', status_code=200)
def list_customers():
    return {'message': 'success', 'data': customers}

@customer_router.put('/{customer_id}', status_code=200)
def edit_customer(customer_id: int, payload: CustomerCreate):
    curr_customer = None
    # get the customer
    for customer in customers:
        if customer.id == customer_id:
            curr_customer = customer
            break
        print (f"current customer is: {curr_customer}")

    if not curr_customer:
        raise HTTPException(status_code=404, detail="customer not found")
    curr_customer.username = payload.username
    curr_customer.address = payload.address
    return {"message": "customer edited successfully", "data": curr_customer}
