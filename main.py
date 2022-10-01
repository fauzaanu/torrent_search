import requests

from SLEZ import Session

terms = ""


def search_terms_gen(term):
    terms = ""
    list = term.split()
    #print(list)

    for term in list:
        terms = terms+f"{term}+"

    if terms[-1] == "+":
        x = len(terms)
        terms = terms[:x-1]
    return terms


search_term = search_terms_gen("rush hour")
print(search_term)


# RARBG DOES NOT LIKE TO BE SCRAPED AND GIVES CAPTCHA
# url = f"https://rarbggo.org/torrents.php?search={search_term}&category[]=17&category[]=44&category[]=45&category[]=47&category[]=50&category[]=51&category[]=52&category[]=42&category[]=46&category[]=54"

url = f"https://magnetdl.torrentbay.to/search/?q={search_term}&m=1&x=0&y=0"


"magnet:?xt=urn:btih:5AB48D67FB69A914353CD86E9A417DC57CF809BC"

headerz = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}


username = 'Fauzaanu'

browser = r"C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
profile = rf'C:\Users\{username}\AppData\Local\BraveSoftware\Brave-Browser\User Data\Profile 3'

selenium_session = Session(browser, profile, headless=False, delay=0)
selenium_session.browse(url)

# magnet links from rarbg
links_xpath_rr = "//td[contains(@class,'lista') and not(contains(@valign,'top'))]//a[contains(@href,'/torrent/') and not(contains(@href,'#comments'))]"

# magnet links from https://magnetdl.torrentbay.to/
links_xpath_mg = "//a[contains(@href,'magnet:?')]"

obj = selenium_session.wait_for_selject(links_xpath_mg,multiple=True)
for ob in obj:
    x = selenium_session.scrape_attribute(ob,attribute='href',tag='a')
    print(x)


selenium_session.close_driver()