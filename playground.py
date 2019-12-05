import requests
from bs4 import BeautifulSoup

url="https://weather.com/weather/today/l/41.97,-71.19?par=google&temp=f"
r=requests.get(url)
text=r.text
soup=BeautifulSoup(text, 'html.parser')
for div in soup.findAll('div', attrs={'class':'today_nowcard-temp'}):
    temp=div.text
    

utemp=int(temp[0:2])

if utemp < 58:
    print("WEAR PANTS TODAY")
elif utemp >= 58:
    print("WEAR SHORTS TODAY")




    


