
README for "Develop Average Calculator Microservice"
Introduction:
This microservice calculates the average of numbers fetched from a test server based on specified criteria such as prime, Fibonacci, even, or random numbers.

How to Use:
Start the microservice.
Send a GET request to /numbers/{numberid} where numberid can be one of the following: 'p' for prime, 'f' for Fibonacci, 'e' for even, and 'r' for random numbers.
Include the access token in the request header to authenticate the request.
Parameters:
numberid: The type of numbers to fetch ('p', 'f', 'e', 'r').
access_token: The access token required for authentication.
Response:
numbers: The fetched numbers based on the specified criteria.
windowPrevState: Previous state of the numbers window.
windowCurrState: Current state of the numbers window.
avg: The average of the current window numbers.
Additional Notes:
Ensure the access token is provided for authentication.
The microservice handles requests within 500 milliseconds.
The window size for storing numbers can be configured.
README for "Develop Top Products HTTP Microservice"
Introduction:
This microservice retrieves top products from various e-commerce companies based on specified category, price range, and sorting criteria.

How to Use:
Start the microservice.
Send a GET request to /categories/{categoryname}/products to fetch top products within a category.
Optionally, include query parameters to specify the number of products, page number, and sorting criteria.
Parameters:
categoryname: The category of products to fetch.
n: Number of products to retrieve (default is 10, maximum is 50).
page: Page number for pagination (default is 1).
sort_by: Sorting criteria (e.g., 'price', 'rating', 'discount').
sort_order: Sorting order ('ascending' or 'descending').
Response:
List of top products within the specified category.
Each product contains attributes like name, price, rating, discount, and availability.
Additional Notes:
The microservice handles pagination for large result sets.
Sorting criteria and order can be specified for customized results.
Ensure the correct category name is provided in the request.
These README files provide a guide on how to use each microservice along with relevant parameters, responses, and additional notes.
