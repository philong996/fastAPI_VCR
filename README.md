# fastAPI_VCR

### Docker

* docker-compose up -d --build
* docker-compose logs -f <docker-name> 
* docker container start <docker-name> 

### API to insert data

```python

### insert customer
customer = {
  "customer_code": "string",
  "gender": "string",
  "birthday": "2020-08-18",
  "district": "string",
  "city": "string",
  "email": "string",
  "first_purchase_date": "2020-08-18",
  "id": 0
}

product = {
  "product_code": "string",
  "category": "string",
  "design_group": "string",
  "price_segment": "string"
}

trans = {
  "trans_code": "string",
  "customer_id": 0,
  "product_id": 0,
  "promotion_id": "string",
  "price": 0,
  "discount": 0,
  "source": "string",
  "store": "string",
  "created_date": "2020-08-18"
}

url = "localhost:8005/customer"
requests.post(url, data = customer)

url = "localhost:8005/product"
requests.post(url, data = product)

url = "localhost:8005/transaction"
requests.post(url, data = trans)
``` 
