
from SLEZ import Session


def search_terms_gen(term):
    terms = ""
    list_terms = term.split()
    # print(list)

    for term in list_terms:
        terms = terms + f"{term}+"

    if terms[-1] == "+":
        x = len(terms)
        terms = terms[:x - 1]
    return terms


def search_torrents(term):
    search_term = search_terms_gen(term)
    # print(search_term)

    # headerz = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
    # Chrome/106.0.0.0 Safari/537.36' } RARBG DOES NOT LIKE TO BE SCRAPED AND GIVES CAPTCHA url =
    # f"https://rarbggo.org/torrents.php?search={search_term}&category[]=17&category[]=44&category[]=45&category[
    # ]=47&category[]=50&category[]=51&category[]=52&category[]=42&category[]=46&category[]=54" url =
    # f"https://magnetdl.torrentbay.to/search/?q={search_term}&m=1&x=0&y=0"

    url_ext = f"https://ext.torrentbay.to/search/?q={search_term}"

    windows = True

    if windows:

        username = 'Fauzaanu'

        browser = r"C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
        profile = rf'C:\Users\{username}\AppData\Local\BraveSoftware\Brave-Browser\User Data\Profile 3'

    else:

        username = 'fauzaanu'

        browser = rf"/opt/brave.com/brave/brave"
        profile = rf'/home/{username}/.config/BraveSoftware/Brave-Browser/Default'

    selenium_session = Session(browser, profile, headless=True, delay=0)

    selenium_session.browse(url_ext)

    # magnet links from rarbg links_xpath_rr = "//td[contains(@class,'lista') and not(contains(@valign,'top'))]//a[
    # contains(@href,'/torrent/') and not(contains(@href,'#comments'))]"

    # magnet links from https://magnetdl.torrentbay.to/
    # links_xpath_mg = "//a[contains(@href,'magnet:?')]"

    # ext is a lot better considering the magnet links are  already available in just one click...

    links_xpath_xt = "//a[contains(@href,'magnet:?')]"

    obj = selenium_session.wait_for_selject(links_xpath_xt, multiple=True)

    torrents = {}
    for ob in obj:
        x = selenium_session.scrape_attribute(ob, attribute='href', tag='a')
        name_xt = f"//tr//a[contains(@href,'{x}')]/../..//b"
        text_sel = selenium_session.wait_for_selject(name_xt)
        z = selenium_session.scrape_content(text_sel)
        # print(z)
        # print(x, z)
        torrents[z] = x
    print(torrents)
    selenium_session.close_driver()
