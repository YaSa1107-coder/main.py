import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

# إعداد السجلات
logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv('BOT_TOKEN')

# دالة الترحيب مع أزرار الربح
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💰 أفضل عروض اليوم", callback_data='deals')],
        [InlineKeyboardButton("📢 قناة العروض الخاصة", url='https://t.me/your_channel')], # ضع رابط قناتك هنا
        [InlineKeyboardButton("🎁 اربح مكافأة يومية", callback_data='reward')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🚀 أهلاً بك في بوت الربح الذكي!\n\n"
        "اختر من القائمة بالأسفل لبدء توفير المال أو كسب الجوائز:",
        reply_markup=reply_markup
    )

# دالة التعامل مع ضغطات الأزرار
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'deals':
        # هنا تضع روابط الآفيليت الخاصة بك (أمازون، نون، إلخ)
        text = "🔥 عروض حصرية لك:\n1- آيفون 15 بخصم 20% [رابطك هنا]\n2- سماعات سوني [رابطك هنا]"
        await query.edit_message_text(text=text)
    
    elif query.data == 'reward':
        await query.edit_message_text(text="للحصول على مكافأتك، قم بزيارة الرابط التالي: [ضع رابط مختصر هنا]")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button_click))
    
    print("البوت المطور انطلق بنجاح...")
    application.run_polling()
