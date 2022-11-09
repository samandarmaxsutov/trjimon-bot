import http.client

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey your_token"
    }

conn.request("GET", "/pray/all?data.city=istanbul", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))