import sys
import logging

log = logging.Logger("alerta")

info = {
    "temperatura": None,
    "umidade": None
}

keys = info.keys()

for key in keys:
    try:
        #temperatura = float(input("Qual é a temperatura atual? ").strip())
        info[key] = float(input(f"Qual é a {key} atual? ").strip())
    except ValueError:
        log.error(f"{key.capitalize()} inválida")
        sys.exit(1)   
        
temperatura = info["temperatura"]
umidade = info["umidade"]

print(temperatura, umidade)

if temperatura > 45:
    print("ALERTA! 🥵 Perigo de calor extremo")
elif temperatura * 3 >= umidade:
    print("ALERTA! 🥵🐳 Perigo de calor úmido")
elif temperatura >= 10 and temperatura <= 30:
    print("😊 Normal")
elif temperatura >= 0 and temperatura <= 10:
    print("🥶 Frio")
elif temperatura < 0:
    print("ALERTA!☃️ Frio extreno")
        
