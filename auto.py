import pyautogui
import random
import time
import keyboard  

# Desativa a trava de segurança dos cantos da tela para evitar paradas acidentais
pyautogui.FAILSAFE = False

largura_tela, altura_tela = pyautogui.size()

print("Iniciando em 3 segundos...")
print("⚠️ PARA PARAR: Segure a tecla 'ESC' a qualquer momento.")
time.sleep(3)

# --- PASSO 1: Minimizar o VS Code ---
# Move o mouse para a posição do botão minimizar (assumindo janela maximizada no Windows)
# O eixo X é a largura total menos cerca de 130 pixels, e o Y é perto do topo (20 pixels)
pyautogui.moveTo(largura_tela - 130, 20, duration=1.0)
pyautogui.click()

# Dá uma pequena pausa para a animação da janela descendo
time.sleep(1)

try:
    while True:
        # 1. Verifica se a tecla de parada foi pressionada antes do movimento
        if keyboard.is_pressed('esc'):
            print("\nPrograma encerrado pelo atalho de teclado (ESC).")
            break

        # 2. Sorteia posições e move o mouse
        x_aleatorio = random.randint(0, largura_tela)
        y_aleatorio = random.randint(0, altura_tela)
        tempo_movimento = random.uniform(0.5, 2.0)
        
        pyautogui.moveTo(x_aleatorio, y_aleatorio, duration=tempo_movimento)
        
        # 3. Pausa "natural" inteligente
        tempo_pausa = random.uniform(2.0, 6.0)
        tempo_inicial = time.time()
        
        while time.time() - tempo_inicial < tempo_pausa:
            if keyboard.is_pressed('esc'):
                print("\nPrograma encerrado pelo atalho de teclado (ESC) durante a pausa.")
                exit() # Sai do programa imediatamente
            time.sleep(0.1)

except KeyboardInterrupt:
    print("\nPrograma encerrado pelo terminal (Ctrl+C).")