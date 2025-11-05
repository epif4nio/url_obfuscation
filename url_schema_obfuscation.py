#!/bin/python3

import sys

URL_TEMPLATE = "http://{}@{}"

if len(sys.argv) != 3:
    print("Usage: ./obfuscate_url.py <fake_address> <real_ip_address>\n" \
    "Example: ./url_schema_obfuscation.py twitter.com/elonmusk 194.150.169.131")
    exit(-1)

fake_addr = sys.argv[1]
real_ip_addr = sys.argv[2]

username_part = (
    fake_addr.replace("http://", "")
    .replace("https://", "")
    .replace("/", "\u2215")
)

ip_parts = real_ip_addr.split(".")
binary_string = ""

for part in ip_parts:
    binary_string += "{0:08b}".format(int(part))

print(URL_TEMPLATE.format(username_part, int(binary_string, 2)))

