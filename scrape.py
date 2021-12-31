from tkinter import *
import requests
from bs4 import BeautifulSoup
from colorama import Fore
import smtplib

URL = "https://www.amazon.co.uk/WATERCOOLING-NZXT-KRAKEN-360MM-RL-KRZ73-01/dp/B084HMGKWT/ref=sr_1_1?keywords=z73&qid=1638467789&sr=8-1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/87.0.4280.141 Safari/537.36"}




def check_price():
    page = requests.get(URL, headers=headers)
    
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "corePrice_desktop").get_text()
    price2 = price[1:4]
    price3 = int(price[1:5])

    if price3 < 240:
        send_mail()

    print(title.strip())
    print(Fore.BLUE + f"Price: {price.strip()}")

    
def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("elyassepahi14@gmail.com","Elyas123!")
    subject = "Price decrease"
    body = "Check amazon link provided, This product has decreased in price - {title})"
    msg = f"Subject: {subject}\n\n{body}"
    print("Email has been successful")
    server.sendmail("elyassepahi14@gmail.com","elyassepahi14@gmail.com",msg)
    server.quit()




check_price()

print("press any key to exit")


#Tkinter part 
root = Tk()
root.title("Amazon Webscraper")
root.geometry("600x600")
mainloop()

