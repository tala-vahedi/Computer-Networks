# import sys module to fetch the command line arguments
import sys
from urllib.parse import urlparse
from pathlib import Path
import os

# function definition to parse url and store in a file
def url_parser(param_url,filename):
    
    #stores the parsed elements into different variables
    url_parsed = urlparse(param_url)
    url = str(param_url)
    host = str(url_parsed.hostname)
    path = str(url_parsed.path)
    port = str(url_parsed.port)

    #checks if the port listed as 'none' and replaces it with '80' 
    if (port == 'None'):
        port = '80'
    
    #checks if a numbers text file already exists
    if os.path.exists(filename):
        append = 'a'
    #if it does exist it adds/appends to other creates a new file
    else: 
        append = 'x'

    #adds the parsed variables to the text file on a new line
    file = open(filename, append)
    file.write("URL: " + url)
    file.write("\n")
    file.write("Host: " + host)
    file.write("\n")
    file.write("Path: " + path)
    file.write("\n")
    file.write("Port: " + port)
    file.write("\n")
    file.write("\n")
    
    #returns the filename
    return filename
    #closes the file
    file.close()

#gets the command line parameters for the url and filename
first_parameter = sys.argv[1]
second_parameter = sys.argv[2]

#function call to parse the url and store in file
stored_file = url_parser(first_parameter, second_parameter)

# display the filename which contains the parsed attributes of the url
print("The parsed attributes are stored in: %s" %stored_file)