import requests

url = "https://lernx.io/Courses/Python-3-Bootcamp/view.php?code=2.7-8"
req = requests.get(url)

print(req.status_code)

if req.status_code == 200:
    content_type = req.headers.get('Content-Type')
    if 'application/json' in content_type:
        # If the response is JSON, parse it
        data = req.json()
        print(data)
    else:
        # If the response is not JSON, print the raw text
        print("Response is not in JSON format")
        print(req.text)
else:
    print(f"Request failed with status code: {req.status_code}")
