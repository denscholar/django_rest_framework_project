import requests

# endpoint = "https://httpbin.org/status/200"
endpoint = "http://localhost:8000/api/"
# endpoint = "http://localhost:8000/products/"


get_response = requests.get(
    endpoint, params={"abc": 123456}, json={"query": "hello world"}
)

# print(type(get_response.text))
print(get_response.json())
