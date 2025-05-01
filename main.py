import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
from telegram import ReplyKeyboardMarkup, KeyboardButton
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import pytz
    # Включаем логирование
logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )

    # Главное меню
main_menu = [
        ["🌲 Хвойные (ель/сосна)", "🍏 Плодовые"],
        ["🌸 Розы и рододендроны", "🪻 Гортензии"],
        ["📊 График подкормок", "🛡️ Обработка участка"]
    ]

reply_markup = ReplyKeyboardMarkup(main_menu, resize_keyboard=True)

    # Команда /start
from telegram import KeyboardButton, ReplyKeyboardMarkup

        # Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buy_button = [[KeyboardButton('🛒 Купить гайд за 1800 ₽')]]
    reply_markup = ReplyKeyboardMarkup(buy_button, resize_keyboard=True)

    await update.message.reply_text(
        "Добро пожаловать в Зелёного Доктора!\n\nВы можете купить профессиональный гайд по гортензиям!",
        reply_markup=reply_markup
    )

    # Обработка кнопок
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text
responses = {
    "🪻 Гортензии": "FILE:gortenzii.pdf",
    "📈 График подкормок": "📄 График подкормок: [скачать PDF](https://yourdomain.com/grafik.pdf)",
    "🌲 Хвойные (ель/сосна)": "📄 Памятка по хвойным: [скачать PDF](https://yourdomain.com/hvoinye.pdf)",
    "🍏 Плодовые": "📄 Памятка по плодовым: [скачать PDF](https://yourdomain.com/plodovye.pdf)"
 }
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    responses = {
        "🪻 Гортензии": "FILE:gortenzii.pdf"
    }

    response = responses.get(text)
    if response:
        if response.startswith("FILE:"):
            filename = response.replace("FILE:", "")
            with open(filename, "rb") as f:
                await update.message.reply_document(f)
        else:
            await update.message.reply_text(response, parse_mode="Markdown")
    else:
        await update.message.reply_text("Пожалуйста, выберите пункт из меню.")

    # Запуск бота
def main():
        app = ApplicationBuilder().token("7445098103:AAFYRydAz4fjzOWddrrM49-ncgw2rAR-n3I").build()

        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
     # Настройка ежедневной публикации историй в канал

# ID твоего канала
CHANNEL_ID = -100513898900

# Список историй для публикации
stories = [
            "🌳 История 1: Как Пётр I завозил липы в Петербург...",
            "🌸 История 2: Легенда о первых сиренях в Летнем саду...",
            "🌲 История 3: Как в Петербурге появились ели и сосны...",
            "🌹 История 4: Ботанические коллекции Екатерины II...",
            "🌿 История 5: Экспедиции за растениями в эпоху дворцов..."
            # Сюда потом легко добавим все остальные истории!
        ]
current_story_index = 0
async def send_story():
    await application.bot.send_message(
        chat_id=CHANNEL_ID,
        text="🌳 История 1: Как Пётр I завозил липы в Петербург...\n\nПётр I лично привозил липы из Европы для озеленения новых садов Санкт-Петербурга! Это был первый крупный проект по созданию зеленых насаждений в суровых северных условиях."
    )
            try:
                await send_story(app.bot)
                await app.bot.send_message(chat_id=CHANNEL_ID, text="🧪 Проверка: бот работает и история отправлена!")
            except Exception as e:
                print(f"Ошибка: {e}")
async def main():
    scheduler = BackgroundScheduler(timezone="Europe/Moscow")
    scheduler.add_job(send_story, trigger='cron', hour=12, minute=0)
    scheduler.start()
    try:
        await send_story(app.bot)
        await app.bot.send_message(chat_id=CHANNEL_ID, text="✏️ Проверка: бот работает и история отправлена!")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
    app.run_polling()


   
