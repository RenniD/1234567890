#7503355405:AAHvGPzFIkZ9SdAnxhHySbrhD07sDw7DssI
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes, ConversationHandler, \
    MessageHandler, filters

#-------------------------------------------------------------------------------
# Стадії конверсії
DATE_START, DATE_END, GUESTS, ROOM_TYPE = range(4)

#-------------------------------------------------------------------------------

app = ApplicationBuilder().token('7503355405:AAHvGPzFIkZ9SdAnxhHySbrhD07sDw7DssI').build()

#-------------------------------------------------------------------------------
#-----------тапа кнопка

async def tap_button(update, context):
    q = update.callback_query
    await q.answer()

#-----------действие

    if q.data == "a":
        await q.message.reply_text(
            "Лютые анекдоты уже скоро\n"
            "2 дня"
        )
    elif q.data == "menu":
        await q.message.reply_text(
            "Лютае меню уже прям скоро скоро"
        )
    elif q.data == "donat":
        await q.message.reply_text(
            "на булочку\n"
            "(4441111137101667)"
        )
    else:
        await q.message.reply_text(
            "попробуйте снова /start"
        )
#-----------
#-------------------------------------------------------------------------------
#запуск

async def start_command(update, context):
    keyboard = [
        [InlineKeyboardButton("Анекдоты", callback_data="a")],
        [InlineKeyboardButton("Меню", callback_data="menu")],
        [InlineKeyboardButton("Донат", callback_data="donat")]
    ]
    markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "UwU",
        reply_markup=markup
    )

#---------------------------------------------------------------------------------

async def data_start(update, context):
    context.user_data['data_start'] = update.message.text
    await update.message.reply_text("Ввудите дату выезда (например, 2027-10-69)")
    return DATE_END

async def data_end(update, context):
    context.user_data['data_end'] = update.message.text
    await update.message.reply_text("Сколько гостей будет👨🏿👩🏿?")
    return GUESTS


async def guests (update, context):
    context.user_data['guests'] = update.message.text
    reply_keyboard = [["24", "47", "98"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text("Сколько гостей будет👨🏿👩🏿?", reply_markup=markup)
    return ROOM_TYPE

async def data_end(update, context):
    context.user_data['data_end'] = update.message.text
    await update.message.reply_text("Сколько гостей будет👨🏿👩🏿?")
    return GUESTS

#-----------------------------------------------------------------------------------

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CallbackQueryHandler(tap_button))

#-----------------------------------------------------------------------------------

# Добавление ConversationHandler для бронирования
booking_handler = ConversationHandler(
    entry_points=[CallbackQueryHandler(button_handler, pattern="^book$")],
    states={
        DATE_START: [MessageHandler(filters.TEXT & ~filters.COMMAND, date_start)],
        DATE_END: [MessageHandler(filters.TEXT & ~filters.COMMAND, date_end)],
        GUESTS: [MessageHandler(filters.TEXT & ~filters.COMMAND, guests)],
        ROOM_TYPE: [MessageHandler(filters.TEXT & ~filters.COMMAND, room_type)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)

app.add_handler(booking_handler)

#-----------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run_polling()
```
