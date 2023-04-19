# QR Code Generator Telegram Bot

This is a Telegram bot that generates QR codes from user-provided text.

## Getting Started

To use the bot, you can send a message to the bot with the "/qr" command followed by the text you want to encode into a QR code. The bot will generate a QR code image and send it back to you.

### Prerequisites

This bot is written in Python 3 and requires the following libraries:

- qrcode
- telebot

You can install these libraries using pip: `pip install qrcode` & `pip install pyTelegramBotAPI`

### Installing

To use the bot, you first need to create a new bot on Telegram and get its API token. You can do this by following these steps:

1. Open the Telegram app and search for the "BotFather" bot.
2. Start a chat with "BotFather" and send the command "/newbot".
3. Follow the instructions provided by "BotFather" to create a new bot and get its API token.

Once you have the API token, you need to replace "YOUR_TELEGRAM_BOT_TOKEN" in the code with your bot's API token.

## Usage

To use the bot, you can send a message to the bot with the "/qr" command followed by the text you want to encode into a QR code. For example:

`/qr https://www.google.com/`

The bot will generate a QR code image from the provided text and send it back to you.

## Contributing

We welcome contributions from everyone. Here are some ways you can contribute:

- Report bugs or suggest new features by opening an issue.
- Write code or documentation by forking the repository and submitting a pull request.

## Authors

**Anurag Dubey**

## License

This project is licensed under the MIT License - see the [License](https://github.com/Anuragd275/qr_code_gen_bot/blob/main/LICENSE) file for details.
