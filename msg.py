import webbrowser
import pyautogui
from time import sleep

# Lista de números de teléfono
numbers = ['+573108520464', '+573157645002', '+573187528853']
message = '🔈¡Atención usuarios de Hooy app! Hoy, domicilios a solo $1.000 pesos en Hooy app, Aprovechen y compren nuestras promos exclusivas por HOOY APP💜 🚀' 

# Abre WhatsApp Web una sola vez
webbrowser.open('https://web.whatsapp.com')
sleep(5)  # Espera suficiente tiempo para escanear el código QR

for number in numbers:
    # Navega a la URL de chat específica
    chat_url = f'https://web.whatsapp.com/send?phone={number}'
    pyautogui.hotkey('ctrl', 'l')  # Selecciona la barra de direcciones
    pyautogui.typewrite(chat_url)
    pyautogui.press('enter')
    sleep(10)  # Espera a que la página cargue el chat

    # Clic en el icono de adjuntar
    pyautogui.click(1250, 980)  # Ajusta las coordenadas según tu pantalla
    sleep(2)
    
    # Clic en el icono de adjuntar imágenes/fotos
    pyautogui.click(1150, 780)  # Ajusta las coordenadas según tu pantalla
    sleep(2)

    # Escribir la ruta de la imagen en el diálogo de selección de archivos
    pyautogui.typewrite(message)
    pyautogui.press('enter')
    sleep(2)  # Espera a que la imagen se cargue en el chat

    # Enviar la imagen
    pyautogui.press('enter')
    sleep(2)  # Espera a que la imagen se envíe antes de proceder al siguiente número