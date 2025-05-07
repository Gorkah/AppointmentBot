# AutoClick-AppointmentBot

Este es un script en Python que automatiza el proceso de clics en pantalla para facilitar tareas repetitivas, como reservar citas en portales web. El comportamiento está pensado para un flujo específico: seleccionar opciones como "Presencial" o "Telefónica" y luego monitorear si aparece una cita disponible.

---

## 🚀 Características

- Permite registrar posiciones de clic con solo presionar `Enter`.
- Automatiza la secuencia de clics indefinidamente.
- Se puede detener fácilmente presionando la tecla `Esc`.
- Ejecutable disponible para usuarios sin Python instalado.

---

## 🧠 ¿Cómo funciona?

1. Al iniciar el script o ejecutable, se minimiza la ventana.
2. Se deben posicionar manualmente los clics de las opciones a seleccionar (ej. "Presencial", "Telefónica"), presionando `Enter` en cada una.
3. Para finalizar la grabación, presiona `Esc`.
4. Luego de un conteo de 5 segundos, comenzará a hacer clic en bucle sobre las posiciones grabadas.
5. Para detener el proceso, simplemente presiona `Esc`.

---

## ⚙️ Requisitos (solo si ejecutas el `.py`)

- Python 3.x
- Bibliotecas:
  - `pyautogui`
  - `keyboard`

Instalación rápida de dependencias:

```bash
pip install pyautogui keyboard
