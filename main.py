from fastapi import FastAPI

app = FastAPI()

items = [
    {"id": 1, "name": "Laptop", "price": 55000},
    {"id": 2, "name": "Mouse", "price": 500},
    {"id": 3, "name": "Keyboard", "price": 1200},
]

@app.get("/list") 
def get_list(): 
    return items

@app.get("/listId")
def get_item(id: int):
    for item in items:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
