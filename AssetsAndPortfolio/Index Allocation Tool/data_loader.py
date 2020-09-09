import requests
from bs4 import BeautifulSoup


def load(url, name):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    link = soup.select('#holdings>div.holdings>a')[0].attrs['href']
    link = f'https://www.ishares.com{link}'

    csv = requests.get(link).text
    with open(f'{name}.csv', "w") as text_file:
        text_file.write(csv)


indizes = {
 'MSCI_EM': 'https://www.ishares.com/ch/intermediaries/en/products/251857/ishares-msci-emerging-markets-ucits-etf-inc-fund?switchLocale=Y',
 'MSCI_EM_small_cap': 'https://www.ishares.com/ch/intermediaries/en/products/251859/ishares-msci-emerging-markets-smallcap-ucits-etf',
 'MSCI_Europe': 'https://www.ishares.com/ch/intermediaries/en/products/251860/ishares-msci-europe-ucits-etf-inc-fund',
 'MSCI_USA_Equal_Weight': 'https://www.ishares.com/us/products/239693/ishares-msci-usa-etf',
 'MSCI_Eastern_Europe': 'https://www.ishares.com/ch/individual/en/products/251855/ishares-msci-eastern-europe-capped-ucits-etf?switchLocale=Y',
 'MSCI_Pacific_ex_japan': "https://www.ishares.com/us/products/239674/ishares-msci-pacific-ex-japan-etf"
}


for name, url in indizes.items():
    load(url, name)