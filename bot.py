import requests
import time

TOKEN = "TU_TOKEN_TELEGRAM"
CHAT_ID = "TU_CHAT_ID"

def enviar_mensaje(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": texto}
    requests.post(url, data=data)

def obtener_precio_binance():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    data = requests.get(url).json()
    return float(data["price"])

def obtener_precio_bybit():
    url = "https://api.bybit.com/v2/public/tickers?symbol=BTCUSDT"
    data = requests.get(url).json()
    return float(data["result"][0]["last_price"])

while True:
    try:
        binance = obtener_precio_binance()
        bybit = obtener_precio_bybit()

        diferencia = bybit - binance

        if abs(diferencia) > 50:
            mensaje = f"ALERTA ARBITRAJE 🚨\nBinance: {binance}\nBybit: {bybit}\nDif: {diferencia}"
            enviar_mensaje(mensaje)

        time.sleep(30)

    except Exception as e:
        print(e)
        time.sleep(30)
