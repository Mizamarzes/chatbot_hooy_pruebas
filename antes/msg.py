import webbrowser
import pyautogui
import pyperclip
from time import sleep

# Lista de números de teléfono
numbers = ['+573108520464', '+573157645002', '+573187528853']
message = '🔈¡Atención usuarios de Hooy app! Hoy, domicilios a solo $1.000 pesos en Hooy app, Aprovechen y compren nuestras promos exclusivas por HOOY APP💜 🚀'

# Abre WhatsApp Web una sola vez
webbrowser.open('https://web.whatsapp.com')
sleep(10)  # Espera suficiente tiempo para escanear el código QR y que se cargue completamente

for number in numbers:
    # Navega a la URL de chat específica
    chat_url = f'https://web.whatsapp.com/send?phone={number}'
    pyautogui.hotkey('ctrl', 'l')  # Selecciona la barra de direcciones
    pyautogui.typewrite(chat_url)
    pyautogui.press('enter')
    sleep(10)  # Espera a que la página cargue el chat

    # Escribir el mensaje
    pyperclip.copy(message)
    sleep(1)  # Espera un poco para asegurar que el mensaje esté escrito

    # Pegar el mensaje desde el portapapeles
    pyautogui.hotkey('ctrl', 'v')
    sleep(2)  # Espera un poco para asegurar que el mensaje esté pegado

    # Presiona Enter para enviar el mensaje
    pyautogui.press('enter')
    sleep(5)  # Espera a que el mensaje se envíe antes de proceder al siguiente número
