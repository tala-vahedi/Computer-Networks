# Computer-Networks

This web_client does the following:
1. Construct the address and port number
2. Construct the http GET request (with Host and Connection headers)
3. Connect to the server, and read the response
4. Save the body of the HTTP response to param_file (skip the header)
5. If the HTTP response is anything rather than 200 OK, write the response header to param_file
6. Close the connection and the file

The url_parser does the following:
1. requests a webpage via a two parameter terminal/command line
2. parses the url for host, port, path and domain
3. writes the parsed items into a text file
