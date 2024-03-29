import qrcode
from telethon.sync import TelegramClient, events
from config import *

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)


@bot.on(events.NewMessage(pattern='/(?i)start'))
async def start(event):
    chat = event.get_chat()
    start_text = "Hello, I'm up and running, send a text to generate QR Code."
    await event.respond(start_text)


@bot.on(events.NewMessage)
async def make_qr(event):
    chat = await event.get_chat()
    qr_data = event.text
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
    caption_text = "Generated by @qr_code_genn_bot"

    await bot.send_file(chat, photo, caption=caption_text)

if __name__ == '__main__':
    print("Bot Started")
    bot.run_until_disconnected()
