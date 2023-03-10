#!/usr/bin/env python3

import getpass
import os
import unicodedata
import logging

from lxml import etree as ET
import requests
from requests.auth import HTTPBasicAuth


def get_usernames(creds):
    endpoint = "/login/service/v4/User"
    response = get_response(endpoint, creds)
    if response.status_code != 200:
        logging.warning(f"non-200 status code from {endpoint}")
        logging.warning("Is the user/password correct?  Is the server down?")
        exit()
    usersEtree = ET.fromstring(response.content)
    users = usersEtree.findall(".//User")
    usernames = sorted([i.attrib["username"] for i in users])
    return usernames


def do_userfiles(usernames, creds, output_dir):
    existing_files = os.listdir(output_dir)

    for username in sorted(usernames):
        if f"{username}.xml" in existing_files:
            continue
        # students have numeric username ending, and are excluded
        if username[-4:].isnumeric():
            continue
        endpoint = f"/login/service/v4/SchemaData/INDIVIDUAL-ACTIVITIES-University/USERNAME:{username}"
        response = get_response(endpoint, creds)
        if response.status_code != 200:
            logging.info(f"non-200 status code from {endpoint}")
            logging.info(f"skipped {username}")
            continue
        with open(f"{output_dir}/{username}.xml", "w", encoding="utf8") as f:
            f.write(unicodedata.normalize("NFKC", response.content.decode("utf-8")))


def get_response(endpoint, creds, limiter=""):
    base_url = "https://webservices.digitalmeasures.com"
    response = requests.get(
        f"{base_url}{endpoint}{limiter}",
        auth=HTTPBasicAuth(creds.get("user"), creds.get("password")),
    )
    return response


# The following section allows this file to be run with `python scrap_userrecords.py`,
# but normally another script will directly call get_usernames() and do_userfiles()
if __name__ == "__main__":
    creds = {"user": "uncw/web_services_vivo", "password": getpass.getpass()}
    usernames = get_usernames(creds)
    output_dir = os.path.join("output", "users")
    do_userfiles(usernames, creds, output_dir)
