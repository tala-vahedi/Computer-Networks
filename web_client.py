
# import necessary modules
import sys
from urllib.parse import urlparse
from socket import *

# obtain the two parameters from commend line
param_url = sys.argv[1]
param_file = sys.argv[2]

# parse the url 
url_parsed = urlparse(param_url)

# get host and path for constructing request
host = url_parsed.hostname
path = url_parsed.path

# initialize port number and set to 80 if None
if url_parsed.port is None:
    port = 80
else:
    port = url_parsed.port

#print(port)
# connect to socket
s = socket(AF_INET, SOCK_STREAM)
s.connect((host, port))

# construct request
request = "GET " + path + " HTTP/1.1\r\n" + "Host: " + host + ":" + str(port) + "\r\n\r\n"

# send request with request encoded in binary
s.send(request.encode())

# receive request and separate header and body
# using recv argument as 4096 as recommended by Python documentation
response = s.recv(4096)
header, body = response.split(b"\r\n\r\n")

# get response header and content type
response_header = header.decode().split("\r\n")[0]
content_type = header.decode().split("\r\n")[-1]

# check for content type to write as string or binary
if "image" in content_type:
    filename = open(param_file, "wb")
    if response_header == "HTTP/1.1 200 OK":
        filename.write(body)
    else:
        filename.write(response_header)
elif "text" in content_type:
    filename = open(param_file, "w")
    if response_header == "HTTP/1.1 200 OK":
        filename.write(body.decode())
    else:
        filename.write(response_header)

# close connection
s.close()

print("\nFinishing downloading ...")