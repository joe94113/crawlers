import requests
from bs4 import BeautifulSoup


UNIXTIME_URL = "https://www.unixtimestamp.com/index.php"
data = {'timestamp': '1605598907', 'Submit': 'Convert'}
re = requests.post(UNIXTIME_URL, data=data)

if re.status_code == 200:
    soup = BeautifulSoup(re.text, 'html.parser')
    print(soup.prettify())
