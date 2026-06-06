import telebot
import requests
import time
import random

TOKEN = "8711112916:AAHeaGYaWu6IrW0DrD6A3qUa53SXqssuSf8"
CHAT_ID = "-1003821702657"
SHOPEE_AFFILIATE_ID = "18326760228"
SHEIN_AFFILIATE_ID = "5115768370"

bot = telebot.TeleBot(TOKEN)

produtos_shopee = [
    {"nome": "Fone Bluetooth", "preco_original": 89.90, "desconto": 45, "categoria": "eletronicos"},
    {"nome": "Tênis Esportivo", "preco_original": 159.90, "desconto": 38, "categoria": "calcados"},
    {"nome": "Mochila Impermeável", "preco_original": 79.90, "desconto": 52, "categoria": "bolsas"},
    {"nome": "Relógio Smart", "preco_original": 199.90, "desconto": 60, "categoria": "eletronicos"},
    {"nome": "Câmera de Segurança", "preco_original": 129.90, "desconto": 41, "categoria": "eletronicos"},
]

produtos_shein = [
    {"nome": "Vestido Floral", "preco_original": 89.90, "desconto": 55, "categoria": "feminino"},
    {"nome": "Conjunto Fitness", "preco_original": 69.90, "desconto": 48, "categoria": "fitness"},
    {"nome": "Bolsa Transversal", "preco_original": 59.90, "desconto": 43, "categoria": "bolsas"},
    {"nome": "Blusa Casual", "preco_original": 49.90, "desconto": 50, "categoria": "feminino"},
]

emojis = ["🔥", "⚡", "💥", "🚨", "🎯", "💰", "🛒", "✨"]

def calcular_preco(preco_original, desconto):
    return round(preco_original * (1 - desconto/100), 2)

def gerar_link_shopee(affiliate_id):
    return f"https://shope.ee/afiliado/{affiliate_id}"

def gerar_link_shein(affiliate_id):
    return f"https://shein.com/afiliado/{affiliate_id}"

def postar_shopee():
    produto = random.choice(produtos_shopee)
    preco_final = calcular_preco(produto["preco_original"], produto["desconto"])
    emoji = random.choice(emojis)
    link = gerar_link_shopee(SHOPEE_AFFILIATE_ID)
    
    mensagem = f"""
{emoji} *OFERTA SHOPEE IMPERDÍVEL!* {emoji}

🛍️ *{produto["nome"]}*

❌ ~~DE: R$ {produto["preco_original"]}~~
✅ *POR: R$ {preco_final}*
📉 *{produto["desconto"]}% DE DESCONTO!*

🔗 [COMPRAR AGORA]({link})

⏰ _Oferta por tempo limitado!_
    """
    
    bot.send_message(CHAT_ID, mensagem, parse_mode="Markdown")

def postar_shein():
    produto = random.choice(produtos_shein)
    preco_final = calcular_preco(produto["preco_original"], produto["desconto"])
    emoji = random.choice(emojis)
    link = gerar_link_shein(SHEIN_AFFILIATE_ID)
    
    mensagem = f"""
{emoji} *OFERTA SHEIN IMPERDÍVEL!* {emoji}

👗 *{produto["nome"]}*

❌ ~~DE: R$ {produto["preco_original"]}~~
✅ *POR: R$ {preco_final}*
📉 *{produto["desconto"]}% DE DESCONTO!*

🔗 [COMPRAR AGORA]({link})

⏰ _Oferta por tempo limitado!_
    """
    
    bot.send_message(CHAT_ID, mensagem, parse_mode="Markdown")

print("Bot iniciado! Postando promoções...")

while True:
    try:
        postar_shopee()
        time.sleep(180)
        postar_shein()
        time.sleep(180)
    except Exception as e:
        print(f"Erro: {e}")
        time.sleep(60)
