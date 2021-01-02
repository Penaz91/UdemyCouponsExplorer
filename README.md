Udemy Coupons Explorer
======================

While surfing around the net I came across udemycoupons.me, an interesting crowd-sourced website that collects coupons for Udemy courses.

After a short analysis, I noticed the website uses Wordpress, which allows me to use the WP-JSON endpoint to gather some data.

This is the result, a small python script that gets title, date and link of the posts to inform me of the available coupons.

Arguments
---------

`--days DAYS` (short version `-d`) allows to select how many days to go back, searching for posts (default: `1`).

`--notify` (short version `-n`) allows to show a notification instead of printing all the results on console.

`--useragent STRING` (short version `-u`) allows to replace the user-agent (default `UdemyCouponsExplorer 0.0.1`).

Notes
-----

This script is meant to run once a day, in full respect of the website that is being scraped, it doesn't perform anything more than retrieving the titles, dates and direct links to the posts.

The objective of this script is just reminding me that there may be something interesting and I could claim the coupon in case.
