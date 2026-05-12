from flask import Flask, request, jsonify
import requests
import os
from datetime import datetime

app = Flask(__name__)

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")
ASAAS_TOKEN = os.environ.get("ASAAS_TOKEN")

FORMAS = {
    "BOLETO": "📄 Boleto",
    "CREDIT_CARD": "💳 Cartão de Crédito",
    "PIX": "⚡ Pix",
    "DEBIT_CARD": "💳 Cartão de Débito",
    "TRANSFER": "🏦 Transferência"
}

def get_customer_name(customer_id):
    headers = {
        "access_token": ASAAS_TOKEN,
        "Content-Type": "application/json"
    }
    r = requests.get(
        f"https://api.asaas.com/v3/customers/{customer_id}",
        headers=headers
    )
    if r.status_code == 200:
        return r.json().get("name", customer_id)
    return customer_id

def send_discord_message(message):
    headers = {
        "Authorization": f"Bot {DISCORD_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {"content": message}
    requests.post(
        f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages",
        headers=headers,
        json=data
    )

def format_date(date_str):
    if not date_str:
        return "—"
    try:
        d = datetime.strptime(date_str[:10], "%Y-%m-%d")
        return d.strftime("%d/%m/%Y")
    except:
        return date_str

def format_value(value):
    if value is None:
        return "—"
    return f"R$ {float(value):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    event = data.get("event")
    payment = data.get("payment", {})

    customer_id = payment.get("customer")
    customer_name = get_customer_name(customer_id)
    value = format_value(payment.get("value"))
    billing = FORMAS.get(payment.get("billingType", ""), payment.get("billingType", "—"))
    description = payment.get("description") or "—"
    due_date = format_date(payment.get("dueDate"))
    payment_date = format_date(payment.get("paymentDate") or payment.get("clientPaymentDate"))
    invoice_url = payment.get("invoiceUrl") or "—"

    if event == "PAYMENT_CREATED":
        message = (
            f"🛒 **NOVA VENDA GERADA**\n"
            f"━━━━━━━━━━━━━━━━━━\n"
            f"👤 Cliente: {customer_name}\n"
            f"💵 Valor: {value}\n"
            f"💳 Forma: {billing}\n"
            f"📋 Processo: {description}\n"
            f"📅 Vencimento: {due_date}\n"
            f"🔗 Link: {invoice_url}\n"
            f"━━━━━━━━━━━━━━━━━━"
        )
        send_discord_message(message)

    elif event in ["PAYMENT_RECEIVED", "PAYMENT_CONFIRMED"]:
        message = (
            f"✅ **VENDA PAGA**\n"
            f"━━━━━━━━━━━━━━━━━━\n"
            f"👤 Cliente: {customer_name}\n"
            f"💵 Valor: {value}\n"
            f"💳 Forma: {billing}\n"
            f"📋 Processo: {description}\n"
            f"📅 Pago em: {payment_date}\n"
            f"━━━━━━━━━━━━━━━━━━"
        )
        send_discord_message(message)

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
