import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()  # This will return entire content.
print (data1)
