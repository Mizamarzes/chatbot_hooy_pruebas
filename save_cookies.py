from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pickle
import time

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')
time.sleep(30)  # Wait for the user to scan the QR code and login manually

# Save cookies to a file
with open('whatsapp_cookies.pkl', 'wb') as file:
    pickle.dump(driver.get_cookies(), file)

print("Cookies have been saved.")
driver.quit()
