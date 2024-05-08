Develop Average Calculator Microservice
Introduction:
This microservice calculates the average of numbers fetched from a test server based on specified criteria such as prime, Fibonacci, even, or random numbers.

How to Use:
Start the microservice.
Send a GET request to /numbers/{numberid} where numberid can be one of the following: 'p' for prime, 'f' for Fibonacci, 'e' for even, and 'r' for random numbers.
Include the access token in the request header to authenticate the request.
Parameters:
numberid: The type of numbers to fetch ('p', 'f', 'e', 'r').
access_token: The access token required for authentication.
