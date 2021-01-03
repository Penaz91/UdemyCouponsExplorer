#!/usr/bin/env python
"""
This file is part of the UdemyCoupons Explorer Project.
Copyright © 2021, Penaz. All Rights Reserved.
The use of this code is governed by the MIT license attached.
See the LICENSE file for the full license.

Created on: 2021-01-01

Author: Penaz
"""
import datetime
import argparse
import requests
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify




DAYS_DEFAULT = 1
DEFAULT_UA = "UdemyCouponsExplorer 0.0.1"


def scrape_results(params, useragent):
    """
    Contacts the WP-JSON endpoint and returns the posts
    """
    response = requests.get(
        "https://udemycoupons.me/wp-json/wp/v2/posts",
        params=params,
        headers={
            "User-Agent": useragent
        })
    return response.json()


def build_parameters(days):
    """
    Builds the GET parameters for the request
    """
    post_date = datetime.datetime.now() - datetime.timedelta(days=days)
    return {
        "_fields": "title,link,date_gmt",
        "per_page": 10,
        "after": post_date.isoformat()
    }


def print_results(results):
    """
    Does a somewhat pretty-print of the results
    """
    for result in sorted(results, key=lambda x: x["date_gmt"], reverse=True):
        print(result["title"]["rendered"])
        print(len(result["title"]["rendered"]) * "-")
        print(f"Date: {result['date_gmt']}")
        print(f"Link: {result['link']}")
        print(50 * "=")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--days", type=int,
                        help="Number of days to go back in the search")
    parser.add_argument("-n", "--notify", action="store_true",
                        help="Show a notification if posts are found")
    parser.add_argument("-u", "--useragent", type=str,
                        help="Set the user agent")
    args = parser.parse_args()
    days = DAYS_DEFAULT
    useragent = DEFAULT_UA
    if args.days:
        days = args.days
    if args.useragent:
        useragent = args.useragent
    parameters = build_parameters(days)
    results = scrape_results(parameters, useragent)
    if args.notify:
        if results:
            # Send notification
            Notify.init("Udemy Coupons Explorer")
            Notify.Notification.new("Udemy Coupons Explorer",
                                    "New coupons available").show()
            Notify.uninit()
    else:
        # Print results
        print_results(results)
