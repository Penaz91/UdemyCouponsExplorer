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


DAYS_DEFAULT = 1


def scrape_results(params):
    """
    Contacts the WP-JSON endpoint and returns the posts
    """
    response = requests.get(
        "https://udemycoupons.me/wp-json/wp/v2/posts",
        params=params,
        headers={
            "User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0)'
                          ' Gecko/20100101 Firefox/15.0.1'
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--days",
                        help="Number of days to go back in the search")
    parser.add_argument("--notify",
                        help="Show a notification if posts are found")
    args = parser.parse_args()
    days = DAYS_DEFAULT
    if args.days:
        days = int(args.days)
    parameters = build_parameters(days)
    result = scrape_results(parameters)
    print(result)
