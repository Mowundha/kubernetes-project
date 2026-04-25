# from fastapi import APIRouter

# router = APIRouter()

# @router.post("/orders")
# def create_order(order: dict):
#     return {
#         "message": "Order created successfully",
#         "order": order
#     }


# import requests
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/order")
# def create_order():
#     product = requests.get("http://product-service:8003/products").json()
#     return {
#         "order": "created",
#         "product": product
#     }



from fastapi import APIRouter
import requests

router = APIRouter()

@router.post("/orders")
def create_order(order: dict):
    return {
        "message": "Order created successfully",
        "order": order
    }

@router.get("/order-with-product")
def create_order_with_product():
    product = requests.get(
        "http://product-service:8003/products"
    ).json()

    return {
        "order": "created",
        "product": product
    }

