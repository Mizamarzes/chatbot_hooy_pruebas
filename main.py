from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from urllib.parse import quote
import time

# Read the message from the file
with open('message.txt', 'r', encoding='utf-8') as file:
    msg = file.read()
msg = quote(msg)

# Read the phone numbers from the file
numbers = []
with open('numbers.txt', 'r', encoding='utf-8') as file:
    for num in file.readlines():
        numbers.append(num.strip())

# Path to the image you want to send
img_hooy = r'F:\codigos\campuslands\proyectos\chatbot_hoy\image_hooy_bot.png'  # Use raw string to handle backslashes

# abrir whatsapp
options = Options()
options.add_argument("user-data-dir=C:/Users/Mizamarzes/AppData/Local/Google/Chrome/User Data")
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://web.whatsapp.com')
time.sleep(20)  


def send_message(num):
    try:
        # Add the country code to the phone number
        phone_number = f'+57{num}'

        # Create the WhatsApp link with the correctly URL-encoded message and image path
        link = f'https://web.whatsapp.com/send?phone={phone_number}'
        driver.get(link)
        time.sleep(10)  # Wait for the chat to load

        # Write the message
        input_element = driver.find_element(By.CLASS_NAME, "x1n2onr6 xh8yej3 lexical-rich-text-input")
        input_element.send_keys(msg + Keys.ENTER)

        print(f"Message sent to {phone_number}")
        time.sleep(5)  # Wait before proceeding to send image

    except Exception as e:
        print(f"Failed to send message to {phone_number}: {e}")

# Loop through each number and send message + image
for num in numbers:
    send_message(num)
    time.sleep(2)  # Wait before moving to the next number

# Wait a sufficient amount of time before closing the browser
time.sleep(10)
driver.quit()
