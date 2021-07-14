import requests
import tkinter as tk
from datetime import datetime
from bs4 import BeautifulSoup
import smtplib

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('nbhagyaraja17@gmail.com','xorqkpifhryuvzym')

    subject = 'Price fell down'
    body = 'Check Doge price : https://www.coindesk.com/price/dogecoin'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'nbhagyaraja17@gmail.com',
        'nbhagyar17@gmail.com',
        msg
    )
    print("Hey Email has been sent!")
    server.quit()

def newtrackdogecoin():
    url = "https://www.coindesk.com/price/dogecoin"
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    title = soup.find("span", { "class" : "coin-iso" }).get_text()
    price = soup.find("div", { "class" : "price-large" }).get_text()
    price = float(price[1:])
    title = title.strip()+" COIN"
    time = datetime.now().strftime("%H:%M:%S")
    labelPrice.config(text=str(price)+" $")
    labelTime.config(text="Updated at :" + time)
    if(price < 0.15):
        send_mail()
    canvas.after(1000, newtrackdogecoin)

canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title("Dogecoin Tracker")

f1 = ("poppins", 24, "bold")
f2 = ("poppins", 22, "bold")
f3 = ("poppins", 18, "normal")

label = tk.Label(canvas, text="DogeCoin Price", font=f1)
label.pack(pady=20)

labelPrice = tk.Label(canvas, font=f2)
labelPrice.pack(pady=20)

labelTime = tk.Label(canvas, font=f3)
labelTime.pack(pady=20)

newtrackdogecoin()

canvas.mainloop()




