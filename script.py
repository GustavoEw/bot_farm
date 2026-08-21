import cv2
import numpy as np
import mss
import pyautogui
import keyboard
import os
import time

PASTA_IMAGENS = "ranked"
CONFIANCA = 0.85

sct = mss.MSS()
monitor = sct.monitors[1]
    

def capturar_tela():
    img = np.array(sct.grab(monitor))
    return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)


def procurar_imagem(tela, caminho):
    template = cv2.imread(caminho)

    if template is None:
        return None

    resultado = cv2.matchTemplate(
        tela,
        template,
        cv2.TM_CCOEFF_NORMED
    )

    _, max_val, _, max_loc = cv2.minMaxLoc(resultado)

    if max_val >= CONFIANCA:
        h, w = template.shape[:2]
        x = max_loc[0] + w // 2
        y = max_loc[1] + h // 2
        return x, y, max_val

    return None


while True:

    # Encerra ao apertar Q
    if keyboard.is_pressed("q"):
        print("Programa encerrado.")
        break

    tela = capturar_tela()

    for arquivo in os.listdir(PASTA_IMAGENS):

        if not arquivo.lower().endswith((".png", ".jpg", ".jpeg")):
            continue

        caminho = os.path.join(PASTA_IMAGENS, arquivo)

        resultado = procurar_imagem(tela, caminho)

        if resultado:
            x, y, conf = resultado

            print(f"{arquivo} encontrado ({conf:.2f})")
            pyautogui.moveTo(x, y, duration=0.05)
            pyautogui.click()

    time.sleep(0.05)