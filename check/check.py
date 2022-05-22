from bs4 import BeautifulSoup
import requests, config, time

url = 'https://nationalhighways.co.uk/travel-updates/the-severn-bridges/'

def run():
    page = requests.get(url, headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"})
    soup = BeautifulSoup(page.content, 'html.parser')

    status = soup.findAll('div', 'severn-crossing-status__heading')
    old_bridge = status[0].text
    new_bridge = status[1].text # not used

    if 'closed' in old_bridge.lower():
        config.insert('Closed', old_bridge, False)
    else:
        config.insert('Open', old_bridge, False)

while True:
    run()
    time.sleep(600)