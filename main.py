from fastapi import FastAPI #, HTTPException 
from routers import spots, sessions

#from typing import List 

app = FastAPI() 

app.include_router(spots.router) #I need to learn what this means
app.include_router(sessions.router)







# grocery_list = [] 

# # Define a Pydantic model for the expected JSON structure in POST requests 
# class GroceryItem(BaseModel): 
#   name: str         # 'name' should be a string 
#   quantity: int     # 'quantity' should be an integer 

# class GroceryItemResponse(BaseModel): 
#   name: str 
#   quantity: int 

# # This endpoint accepts POST requests with JSON data matching the GroceryItem model 
# @app.post("/grocery", response_model=List[GroceryItemResponse]) 
# def add_grocery_item(item: GroceryItem):
#   grocery_list.append({"name": item.name, "quantity": item.quantity})  
#   return grocery_list 

# @app.get("/grocery", response_model=List[GroceryItemResponse])  
# def read_grocery_list():
#   return grocery_list 


# # Path parameter: Retrieve item by its index  
# @app.get("/grocery/{item_id}", response_model=GroceryItemResponse)  
# def get_grocery_item(item_id: int):  
#   if 0 <= item_id < len(grocery_list):
#     return grocery_list[item_id]
#   raise HTTPException(status_code=404, detail="Grocery item with the given ID does not exist. ") 


