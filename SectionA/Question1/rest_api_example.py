import requests

# Send a GET request to the API endpoint
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# Check the status code of the response
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print(data)
else:
    print('Error:', response.status_code)
