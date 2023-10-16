import requests
import lxml.html

# GLOBAL VARS
DOMAIN = "https://store.steampowered.com/explore/new/"

html = requests.get(DOMAIN)
doc = lxml.html.fromstring(html.content)
popular_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]
title = popular_releases.xpath("//div[@class='tab_item_name']/text()")
price = popular_releases.xpath(".//div[@class='discount_final_price']/text()")
tags = [tags.text_content() for tags in \
        popular_releases.xpath(".//div[@class='tab_item_top_tags']")
        ]
tags = [tag.split(",") for tag in tags]
total_platforms = []
platforms = popular_releases.xpath(".//div[@class='tab_item_details']")
span = ""
for platform in platforms:
    span = platform.xpath(".//span[contains(@class, 'platform_img')]")

print(span)
    
    
