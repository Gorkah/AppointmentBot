#Codigo python
import pyautogui
import time
import keyboard
# Función para definir los clicks que se realizarán
def set_click_positions():
    positions = []
    print("Ubica el cursor en la posición y presiona 'Enter' para grabar la posición. Presiona 'Esc' para finalizar.")
   
    while True:
        print("Presiona 'Enter' para grabar la posición actual del cursor o 'Esc' para finalizar.")
       
        while True:
            if keyboard.is_pressed('enter'):
                x, y = pyautogui.position()
                positions.append((x, y))
                print(f"Posición guardada: {x}, {y}")
                time.sleep(0.5)  # Evita múltiple detección de una sola tecla
                break
            elif keyboard.is_pressed('esc'):
                print("Finalizando grabación de posiciones.")
                return positions

    return positions

# Función para realizar los clicks de forma ilimitada hasta que se presione 'Esc'
def perform_clicks(positions, delay=1):
    try:
        while True:
            for position in positions:
                if keyboard.is_pressed('esc'):
                    print("Deteniendo los clicks.")
                    return
                pyautogui.moveTo(position[0], position[1])
                pyautogui.click()
                print(f"Click en: {position[0]}, {position[1]}")
                time.sleep(delay)
    except KeyboardInterrupt:
        print("Proceso interrumpido manualmente.")

if __name__ == "__main__":
    # Configura las posiciones de los clicks
    click_positions = set_click_positions()

    # Realiza los clicks de forma ilimitada
    if click_positions:
        print("Iniciando los clicks en 5 segundos...")
        time.sleep(5)  # Espera 5 segundos antes de comenzar
        perform_clicks(click_positions)
    else:
        print("No se grabaron posiciones de clicks.")