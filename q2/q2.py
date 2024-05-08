from fastapi import FastAPI, HTTPException, Query, Path
from typing import Optional
import requests
import uvicorn

app = FastAPI()


@app.get("/categories/{categoryname}/products")
async def get_top_products(categoryname: str,
                            n: int = Query(..., gt=0, le=50),
                            page: int = Query(1, gt=0),
                            sort_by: Optional[str] = None,
                            sort_order: Optional[str] = None):
   
    url = f"http://20.244.56.144/products/{categoryname}"

    # adding query parameters
    params = {
        "limit": n,
        "page": page,
        "sort_by": sort_by,
        "sort_order": sort_order
    }

    try:
       
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
       
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/categories/{categoryname}/products/{productid}")
async def get_product_details(categoryname: str, productid: str = Path(..., description="The ID of the product")):
   
    url = f"http://20.244.56.144/products/{categoryname}/{productid}"

    try:
        
        response = requests.get(url)

        response.raise_for_status()

       
        return response.json()

    except requests.RequestException as e:
       
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=9945)
