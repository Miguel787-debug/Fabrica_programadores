import pyautogui

pyautogui.press("win")
pyautogui.sleep(1)
pyautogui.write('Google Chrome', interval=0.1)
pyautogui.press('enter')
pyautogui.sleep(3)

pyautogui.write('https://prefeitura.santanadeparnaiba.sp.gov.br/Plataforma/smti/fabrica-de-programadores', interval= 0.1)
pyautogui.sleep(1)
pyautogui.press('enter')

# (0,92) (1892,1011)
pyautogui.hotkey('win','shift','s')
pyautogui.moveTo(0,92, duration= 0.5)
pyautogui.mouseDown()
pyautogui.moveTo(1892,1011, duration= 0.5)
pyautogui.mouseUp()

pyautogui.press("win")
pyautogui.sleep(1)
pyautogui.write('Paint', interval=0.1)
pyautogui.sleep(1)
pyautogui.press('enter')
pyautogui.hotkey('Ctrl', 'v')

