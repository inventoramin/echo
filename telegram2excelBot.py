import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
import gspread
from google.oauth2.service_account import Credentials

# Google Sheets setup (replace with your own values)
SERVICE_ACCOUNT_FILE = '/etc/secrets/service_account.json'  # Path to your service credentials JSON
SHEET_NAME = 'test'  # Sheet name (not file name!)

# Authorize and connect to Google Sheets
creds = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
)
client = gspread.authorize(creds)
sheet = client.open(SHEET_NAME).sheet1  # Opens the first worksheet

async def echo_and_log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    # Reply to Telegram
    await update.message.reply_text(text)
    # Append to Google Sheet
    username = update.message.from_user.username or "NoUsername"
    sheet.append_row([username, text])

def main():
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        raise ValueError("Please set the TELEGRAM_BOT_TOKEN environment variable.")
    application = Application.builder().token(token).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_and_log))
    application.run_polling()

if __name__ == '__main__':
    main()
