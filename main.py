
import smtplib
import requests
import time
from bs4 import BeautifulSoup

url = "https://www.hepsiburada.com/xiaomi-redmi-note-9-pro-64-gb-xiaomi-turkiye-garantili-p-HBV00000TOOB4?magaza=Hepsiburada"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
url  = input("Enter your product link from hepsiburada.com: ")
productPrice = input("Enter the price you expect:")
def checkPrice():
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    title = soup.find(id='product-name').get_text().strip()
    title = title[0:18]
    print(title)
    span = soup.find(id='offering-price')
    content = span.attrs.get('content')
    price = float(content)
    if(price<float(productPrice)):
        sendMail(title)

def sendMail(title):
    sender ='excercisepythonbot@gmail.com'
    reciever = input("Enter your email address:")
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()   
        server.login(sender,'excercisepythonbot61')
        subject = "The product "+ title+ " has dropped to the price you want"
        body = 'You can access the product from this link => '+ url
        mailContent = f"To:{reciever}\nFrom:{sender}\nSubject:{subject}\n\n{body}"
        server.sendmail(sender,reciever,mailContent)
        print('Mail sent successfully.')
    except smtplib.SMTPException as e:
        print(e)
    finally:
        server.quit()

while(1):
    checkPrice()
    time.sleep(60*60)