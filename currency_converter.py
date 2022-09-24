from bs4 import BeautifulSoup as bs
import requests


def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = bs(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:-4])
    
    return rate

dollars = float(input("how much money do you have? "))
incurr = (input("what currency is your money in? "))
outcurr = (input("type a currency you want to convert your money to. ")) 

current_rate = get_currency(f"{incurr}",f"{outcurr}")

total = float(current_rate) * float(dollars)



print(f"{dollars} {incurr} is {total} {outcurr}")

    


