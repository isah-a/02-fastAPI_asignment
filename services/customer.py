from fastapi import HTTPException
from schema.customer import customers

# Function to check if username already exists
class UniqueCustomer:

    @staticmethod
    def check_unique_username(username: str):
        for customer in customers:
            if customer.username == username:
                raise HTTPException(status_code=400, detail="Username already exists")
        return username
    
check_username = UniqueCustomer()