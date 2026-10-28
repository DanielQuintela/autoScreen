import pyautogui
import random
import time

# Obtém o tamanho da tela
largura_tela, altura_tela = pyautogui.size()

print("Iniciando em 3 segundos...")
print("⚠️ PARA PARAR: Arraste o mouse rapidamente para qualquer canto da tela.")
time.sleep(3)

# --- PASSO 1: Minimizar o VS Code ---
# Move o mouse para a posição do botão minimizar (assumindo janela maximizada no Windows)
# O eixo X é a largura total menos cerca de 130 pixels, e o Y é perto do topo (20 pixels)
pyautogui.moveTo(largura_tela - 130, 20, duration=1.0)
pyautogui.click()

# Dá uma pequena pausa para a animação da janela descendo
time.sleep(1)

# --- PASSO 2: Movimentação natural infinita ---
try:
    while True:
        # Sorteia uma posição aleatória na tela
        x_aleatorio = random.randint(0, largura_tela)
        y_aleatorio = random.randint(0, altura_tela)
        
        # Move o mouse com uma velocidade aleatória (mais humano)
        tempo_movimento = random.uniform(0.5, 2.0)
        pyautogui.moveTo(x_aleatorio, y_aleatorio, duration=tempo_movimento)
        
        # Pausa "natural" com duração aleatória antes do próximo movimento (ex: entre 1 e 5 segundos)
        tempo_pausa = random.uniform(1.0, 5.0)
        time.sleep(tempo_pausa)

except KeyboardInterrupt:
    print("\nPrograma encerrado pelo usuário.")
except pyautogui.FailSafeException:
    print("\nPrograma encerrado pela trava de segurança.")