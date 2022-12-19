"""Panorama provisioning script.

This script will provision an instance of Palo Alto Networks Panorama.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
  http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

(c) 2022 Calvin Remsburg
"""
# standard library
import os
import json
import argparse

# third party library
import requests
from dotenv import load_dotenv

# import pandas as pd
# from tabulate import tabulate

# Palo Alto Networks
from panos.panorama import Panorama, DeviceGroup
from panos.objects import Tag

# ----------------------------------------------------------------------------
# Look in our .env file on our computer to locate our credientials
# ----------------------------------------------------------------------------
load_dotenv(".env")

# load Palo Alto Panorama parameters
PANURL = os.environ.get("PANURL", "panorama.lab")
PANUSER = os.environ.get("PANUSER", "automation")
PANPASS = os.environ.get("PANPASS", "mysecretpassword")
pan = Panorama(PANURL, PANUSER, PANPASS)

# load Nautobot parameters
NAUTOBOT_URL = os.environ.get("NAUTOBOT_URL", "nautobot.lab")
NAUTOBOT_TOKEN = os.environ.get("NAUTOBOT_TOKEN", "mytoken")
NAUTOBOT_GRAPHQL = os.environ.get("NAUTOBOT_GRAPHQL", "graphql_uuid")


def grab_nautobot_data():
    """
    Description: Pull down data from Nautobot.
    Workflow:
        1. POST to Nautobot API to execute a GraphQL query
        2. Return output data
    """

    url = f"http://{NAUTOBOT_URL}/api/extras/graphql-queries/{NAUTOBOT_GRAPHQL}/run/"

    payload = json.dumps(
        {"variables": {"device_id": "ea23f4f3-880f-45cd-b67d-7af5bc846c8e"}}
    )
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token {NAUTOBOT_TOKEN}",
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    nautobot_data = response.json()

    return nautobot_data["data"]["device"]


def build_tags(device_config):
    """
    Description: create tag objects for Panorama.
    Workflow:
        1. Pull data from Nautobot GraphQL query
        2. Loop over list of tags, creating each entry.
    Return: None
    """

    # build tags
    if device_config:
        for each in device_config["config_context"]["tag"]:
            color = Tag.color_code(each["color"])
            tag = Tag(name=each["name"], color=color, comments=each["comments"])
            pan.add(tag)
            tag.create()


def main():
    """
    Description: Main execution of our script.
    Workflow:
        1. Pull down device configuration details from Nautobot
        2. Retrieve the config argument passed by the user
        3. Call the appropriate configuration function
        4. Print result to console
    """
    # collect configuration data from Nautobot
    device_config = grab_nautobot_data()

    # create instance of argparse, asking for `--config` to be passed at run
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, required=True)
    args = parser.parse_args()

    # inform user that a configuration build process is taking place
    print(f"Building configuration for {args.config}s")

    # user argument will determine configuration
    if args.config == "tag":

        # build configuration objects
        build_tags(device_config)

    else:
        print("No configuration parameter matched, exiting...")


if __name__ == "__main__":
    main()
