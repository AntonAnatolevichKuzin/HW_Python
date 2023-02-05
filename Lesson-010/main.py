from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import input_date as id
from calculate import operation

heap = {
    'count': 0,
    'first': None,
    'second': None,
    'operator': None
}


async def startcalc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    heap['count'] = 1
    await update.message.reply_text("Что будем считать?")


async def output_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    heap['count'] = 1
    await update.message.reply_text('Для использоваания калькулятора, '
                                    'введите значения аргументов, а затем знак операции'
                                    '(каждое значение аргумента и знак разделяются "Enter")')


async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if heap['count'] != 0:
        if heap['count'] == 1:
            heap['first'] = update.message.text
            heap['count'] += 1
        elif heap['count'] == 2:
            heap['second'] = update.message.text
            heap['count'] += 1
        elif heap['count'] == 3:
            heap['operator'] = update.message.text
            # здесь калькулятор
            a, b = id.inp(heap["first"], heap["second"])
            await update.message.reply_text(f"{a} {heap['operator']} {b} = {operation(a, b, heap['operator'])}")
            heap['count'] = 0
            heap['first'] = None
            heap['second'] = None
            heap['operator'] = None


app = ApplicationBuilder().token("").build()
print("Работаем!!!")
app.add_handler(CommandHandler("start", startcalc))
app.add_handler(CommandHandler("instruction", output_help))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))

app.run_polling()
