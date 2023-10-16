import requests
import lxml.html

# GLOBAL VARS
DOMAIN = "https://store.steampowered.com/explore/new/"
HTML = requests.get(DOMAIN)
STATUS = HTML.status_code

def extrator(html):
    """ Scrape the HTML content of the target domain """

    doc = lxml.html.fromstring(html.content)
    popular_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]

    titles = popular_releases.xpath("//div[@class='tab_item_name']/text()")
    prices = popular_releases.xpath(".//div[@class='discount_final_price']/text()")
    tags = [tags.text_content() for tags in \
            popular_releases.xpath(".//div[@class='tab_item_top_tags']")
            ]
    tags = [tag.split(",") for tag in tags]

    total_platforms = []
    platforms = popular_releases.xpath(".//div[@class='tab_item_details']")

    for platform in platforms:
        temp = platform.xpath(".//span[contains(@class, 'platform_img')]")
        temp = [t.get("class").split(" ")[-1] for t in temp]
        # if "hmd_separator" in temp:
        #     total_platforms.remove("hmd_separator")
        total_platforms.append(temp)

    output = []
    for data in zip(titles, prices, tags, total_platforms):
        reprs = {}
        reprs["titles"] = data[0]
        reprs["prices"] = data[1]
        reprs["tags"] = data[2]
        reprs["total_platforms"] = data[3]
        output.append(reprs)
        
    print(list(zip(titles, prices, tags, total_platforms)))

if __name__ == "__main__":
    if STATUS == 200:
        extrator(HTML)