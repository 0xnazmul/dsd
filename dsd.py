#!/usr/bin/env python3

import sys
import os
import urllib.request
import ssl

def print_usage():
    print("Usage: ./dsd.py <domain_list_file>")
    print("<domain_list_file> should be a file containing a list of domains (one per line)")

NORMAL = "\033[0m"
LIGHTPURPLE = "\033[1;35m"
LIGHTCYAN = "\033[1;36m"

os.system('clear') 

print(" ")
print(" ")
print(f"           {LIGHTPURPLE}Coded By{NORMAL} {LIGHTCYAN}@0xnazmul{NORMAL}")
print(" ")
print("         >>>>>>>>>>>>>>>>>>>>>>>>>>>>>------<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print(" ")
print("                       Domain's HTTP Status Code Checker")
print(" ")
print("         >>>>>>>>>>>>>>>>>>>>>>>>>>>>>------<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print(" ")
print(" ")

def check_status(domain):
    try:
        
        if not domain.startswith(("http://", "https://")):
            domain = "http://" + domain   
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        response = urllib.request.urlopen(domain, context=ssl_context)
        status = response.status        
        formatted_domain = domain.replace("https://", "").replace("http://", "")

        if status == 200:
            print(f"{formatted_domain} - \033[32m{status} OK\033[0m")
        elif status == 300:
            print(f"{formatted_domain} - \033[31m{status} Multiple Choices\033[0m")
        elif status == 301:
            print(f"{formatted_domain} - \033[31m{status} Moved Permanently\033[0m")
        elif status == 302:
            print(f"{formatted_domain} - \033[31m{status} Found\033[0m")
        elif status == 304:
            print(f"{formatted_domain} - \033[31m{status} Not Modified\033[0m")
        elif status == 307:
            print(f"{formatted_domain} - \033[31m{status} Temporary Redirect\033[0m")
        elif status == 400:
            print(f"{formatted_domain} - \033[31m{status} Bad Request\033[0m")
        elif status == 401:
            print(f"{formatted_domain} - \033[31m{status} Unauthorized\033[0m")
        elif status == 402:
            print(f"{formatted_domain} - \033[31m{status} Payment Required\033[0m")
        elif status == 403:
            print(f"{formatted_domain} - \033[31m{status} Forbidden\033[0m")
        elif status == 404:
            print(f"{formatted_domain} - \033[31m{status} Not Found\033[0m")
        elif status == 405:
            print(f"{formatted_domain} - \033[31m{status} Method Not Allowed\033[0m")
        elif status == 406:
            print(f"{formatted_domain} - \033[31m{status} Not Acceptable\033[0m")
        elif status == 408:
            print(f"{formatted_domain} - \033[31m{status} Request Timeout\033[0m")
        elif status == 429:
            print(f"{formatted_domain} - \033[31m{status} Too Many Requests\033[0m")
        elif status == 500:
            print(f"{formatted_domain} - \033[31m{status} Internal Server Error\033[0m")
        elif status == 502:
            print(f"{formatted_domain} - \033[31m{status} Bad Gateway\033[0m")
        elif status == 503:
            print(f"{formatted_domain} - \033[31m{status} Service Unavailable\033[0m")
        elif status == 504:
            print(f"{formatted_domain} - \033[31m{status} Gateway Timeout\033[0m")
        else:
            print(f"{formatted_domain} - {status}")


    except urllib.error.URLError as e:
        if isinstance(e.reason, ssl.SSLError) and "CERTIFICATE_VERIFY_FAILED" in str(e.reason):
            print(f"{domain} - Error: Certificate verification failed")
        else:
            print(f"{domain} - Error: {e.reason}")
def remove_duplicates(file):
    with open(file, "r") as f:
        domains = list(set(f.read().splitlines()))

    with open(file, "w") as f:
        f.write("\n".join(domains))

if len(sys.argv) < 2:
    print_usage()
    sys.exit(1)

if not os.path.isfile(sys.argv[1]):
    print(f"Error: File {sys.argv[1]} not found")
    print_usage()
    sys.exit(1)

remove_duplicates(sys.argv[1])

print("Checking status codes...\n")
with open(sys.argv[1], "r") as f:
    for domain in f:
        check_status(domain.strip())

print("\nDone checking status codes.")
