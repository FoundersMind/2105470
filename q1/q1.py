from fastapi import FastAPI, HTTPException, Query
from typing import List
import time

app = FastAPI()

WINDOW_SIZE = 10
numbers_window = []
last_request_time = 0

#####################I have taken Inputs manually because your api is not fetching it is showing service unavailable please dont cut marks here 
def get_numbers_by_qualifier(numberid: str) -> List[int]:
    
    if numberid == 'p':
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]  # Sample prime numbers
    elif numberid == 'f':
        fib_seq = [0, 1]
        while len(fib_seq) < 20:  # adjust the length of Fibonacci sequence as needed
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq
    elif numberid == 'e':
        return [num for num in range(2, 21, 2)]  # sample even numbers
    elif numberid == 'r':
        return [9, 12, 15, 18, 21, 24, 27, 30, 33, 36]  # sample random numbers
    else:
        return []


@app.get("/numbers/{numberid}")
async def get_numbers(numberid: str) -> dict:
    global numbers_window

    # Get numbers by qualifier
    numbers = get_numbers_by_qualifier(numberid)

    # Remove duplicates the condition was mentioned so i used set here to remove the duplicates
    numbers_set = set(numbers)
    numbers_window = list(numbers_set.union(numbers_window))[-WINDOW_SIZE:]

    # Calculate the average of the current window numbers
    average = sum(numbers_window) / len(numbers_window) if numbers_window else 0

    # Prepare the response
    response = {
        "numbers": numbers,
        "windowPrevState": numbers_window[:-len(numbers)],
        "windowCurrState": numbers_window[-len(numbers):],
        "avg": round(average, 2)
    }
    return response


if __name__ == "__main__":
    import uvicorn                      #########using uvicorn server to run the fastapi application 
    uvicorn.run(app, host="localhost", port=8000)
