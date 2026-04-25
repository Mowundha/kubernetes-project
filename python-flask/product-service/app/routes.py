from fastapi import APIRouter

router = APIRouter()

@router.get("/products/")
def get_products():
    return [
        {"id": 101, "name": "Laptop"},
        {"id": 102, "name": "Phone"}
    ]