# Test Server Registration
## My email is njbhandari4@gmail.com using which i got shortlisted ,In the registering i have used Kiit email 2105470@kiit.ac.in  to make it professional please dont ignore that 
## Introduction:
To access the APIs provided by the test server for the Top Products HTTP Microservice, you need to register your application with the test server. This README provides a step-by-step guide on how to register your application and obtain the necessary access token.

## Steps to Register:
1. **Navigate to Test Server Registration Page**: Visit the registration page of the test server using the provided URL.
![Screenshot 2024-05-08 104434](https://github.com/Sakhtiman/2105470/assets/134630688/2595d300-e70a-49ff-8996-86e15fb5d78e)


2. **Retrieve Access Token**: With your application registered, you can now retrieve an access token to authenticate requests to the test server's APIs. Follow the provided instructions or refer to the test server's documentation on how to obtain an access token using your client credentials.

3. **Use Access Token**: Once you have obtained the access token, you can use it to authenticate requests to the test server's APIs. Include the access token in the request headers as an authorization token (Bearer token) whenever you make API calls.

## Example:
Here's an example of how to use the access token in your API requests using cURL:

```bash
curl -X GET \
  'http://test-server.com/api/endpoint' \
  -H 'Authorization: Bearer your-access-token'

## Average Calculator Microservice

### Introduction:
This microservice calculates the average of numbers fetched from a test server based on certain criteria such as prime, Fibonacci, even, or random numbers. It exposes a REST API endpoint for retrieving these numbers along with their average.
(I have taken manually because the API was not working which was given by you 
### How to Use:
1. Start the microservice.
2. Send a GET request to `/numbers/{numberid}` to retrieve numbers based on the specified criteria.
3. Specify the following parameters in the request:
   - `numberid`: The qualified number ID ('p' for prime, 'f' for Fibonacci, 'e' for even, 'r' for random numbers).
   - `access_token`: Optional. The access token for authentication.
4. The response includes the fetched numbers, the previous and current state of the window, and the average of the current window numbers.
5.Here i am getting service unavailable
![Screenshot 2024-05-08 121806](https://github.com/Sakhtiman/2105470/assets/134630688/16d426b4-d69c-4897-b2d7-4001dacc5c57)
6.So i take manually and got this output which is correct
![Screenshot 2024-05-08 113220](https://github.com/Sakhtiman/2105470/assets/134630688/38db7030-15ad-48f2-9a94-6499943853e1)

### Parameters:
- `numberid`: The qualified number ID ('p' for prime, 'f' for Fibonacci, 'e' for even, 'r' for random numbers).
- `access_token`: Optional. The access token for authentication.

### Response:
- The response includes the fetched numbers, the previous and current state of the window, and the average of the current window numbers.


## Top Products HTTP Microservice

### Introduction:
This microservice provides a public API for retrieving top products from multiple e-commerce companies within specified categories and price ranges. Users can compare products across different companies without needing to register individually with each company.

### How to Use:
1. Start the microservice.
2. Send a GET request to `/categories/{categoryname}/products` to retrieve top products within a category.
3. Specify the following parameters in the request:
   - `categoryname`: The name of the product category.
   - `n`: The number of products to retrieve (maximum 50).
   - `page`: The page number for pagination (default is 1).
   - `sort_by`: Optional. Sort products by rating, price, company, or discount.
   - `sort_order`: Optional. Specify the sort order as ascending or descending.
4. Optionally, send a GET request to `/categories/{categoryname}/products/{productid}` to get details of a specific product.
   - `productid`: The unique ID of the product.
Getting error 404 because Api fetching is not available from your side due to server load
![image](https://github.com/Sakhtiman/2105470/assets/134630688/d6293059-399a-454e-bd5b-092b3de6e13b)

### Parameters:
- `categoryname`: The name of the product category.
- `n`: The number of products to retrieve.
- `page`: The page number for pagination.
- `sort_by`: Optional. Sort products by rating, price, company, or discount.
- `sort_order`: Optional. Specify the sort order as ascending or descending.

### Response:
- The response includes details of the top products within the specified category, including their names, prices, ratings, discounts, and availability.

### Additional Notes:
- Ensure that the requested parameters are valid and within the specified limits.
- Pagination is enforced if the number of products exceeds 10.
- The microservice accommodates changes made by e-commerce companies to the product data.
