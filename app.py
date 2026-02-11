from flask import Flask, request
from datetime import datetime
import requests

app = Flask(__name__)

def detectar_dispositivo(user_agent):
    if "Android" in user_agent or "iPhone" in user_agent:
        return "Celular"
    elif "Windows" in user_agent or "Mac" in user_agent or "Linux" in user_agent:
        return "Computador"
    else:
        return "Desconhecido"

@app.route("/")
def home():
    ip = request.remote_addr
    user_agent = request.headers.get("User-Agent")
    dispositivo = detectar_dispositivo(user_agent)
    horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    geo = requests.get(f"http://ip-api.com/json/{ip}").json()
    cidade = geo.get("city")
    estado = geo.get("regionName")
    pais = geo.get("country")
    isp = geo.get("isp")

    print("===== NOVO ACESSO =====")
    print("IP:", ip)
    print("Cidade:", cidade)
    print("Estado:", estado)
    print("País:", pais)
    print("ISP:", isp)
    print("Dispositivo:", dispositivo)
    print("Horário:", horario)
    print("=======================")

    return "<h1>Projeto Escolar - Monitoramento HTTP</h1><p>Acesso registrado.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
