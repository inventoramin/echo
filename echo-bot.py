from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

def main():
    application = Application.builder().token("7943224731:AAE5IYkiEQwmCkP9C59y5h2QV59cjOm0NXc").build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling()

if __name__ == '__main__':
    main()
