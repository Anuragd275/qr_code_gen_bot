# Importing necessary libraries
from flask import Flask
import qrcode
import telebot
from functions import * # Importing custom functions from 'functions.py'
app = Flask(__name__)

@app.route('/')
def func():
   
    # Telegram Bot API Token
    TOKEN = "6213546095:AAHZAn1B2wzzjyFkV6bA_4JxvtRPvx7Fa3Q"
    bot = telebot.TeleBot(TOKEN)

    # Setting the bot's username for generating QR code caption
    bot_username = "@qr_code_gen_bot"

    # Handler for /start and /help commands
    @bot.message_handler(commands=["start", "help"])
    def welcome(message):
        # Getting chat ID
        chat_id = message.chat.id
        # Sending a welcome message
        bot.send_message(chat_id, "Hi, I'm Alive, How can I help you?")

    # Handler for /qr command
    @bot.message_handler(commands=["qr"])
    def qr_code(message):
        # Getting chat ID
        chat_id = message.chat.id
        # Getting full message text
        full_message = message.text
        # Extracting the string to be encoded from the message
        qr_data = extract_string(full_message, "/qr")

        # Creating a new QR code 
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=4,
        )

        # Adding data to the QR code 
        qr.add_data(f'{qr_data}')

        # Generating the QR code
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qr.png")
        photo = open('qr.png', 'rb')

        # Generating the QR code caption
        caption_text = f"{bot_username}"

        # Sending the QR code image to the user
        try:
            bot.send_photo(chat_id, photo, caption= f"Generated by: {caption_text}")
        except:
            bot.send_message(chat_id, "Could not generate QR for the given url, please try again!")

    # Starting the bot's infinity polling
    bot.infinity_polling()
