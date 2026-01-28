import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

# إعداد السجلات لمراقبة أداء البوت
logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv('BOT_TOKEN')

# القائمة الرئيسية (الترحيب)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    
    # تصميم الأزرار الاحترافية
    keyboard = [
        [InlineKeyboardButton("🛒 عروض AliExpress", callback_query_data='ali')],
        [InlineKeyboardButton("⚡ صفقات Temu", callback_query_data='temu')],
        [InlineKeyboardButton("📦 بالجملة من Alibaba", callback_query_data='alibaba')],
        [InlineKeyboardButton("📢 قناة التخفيضات", url='https://t.me/YourChannel')] # ضع رابط قناتك هنا
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = (
        f"أهلاً بك يا {user_name} في عالم التوفير! 👋\n\n"
        "أنا مساعدك الذكي لجلب أقوى الخصومات من أكبر المتاجر العالمية.\n"
        "يرجى اختيار المتجر الذي تود تصفح عروضه اليوم: 👇"
    )
    
    await update.message.reply_text(text=welcome_text, reply_markup=reply_markup)

# التعامل مع ضغطات الأزرار
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'ali':
        text = (
            "🔥 **أقوى عروض AliExpress اليوم:**\n\n"
            "1- قسم الـ 0.99$ [ضع رابطك هنا]\n"
            "2- كوبونات خصم تصل لـ 12$ [ضع رابطك هنا]\n\n"
            "⚠️ الروابط تتحدث يومياً!"
        )
        await query.edit_message_text(text=text, parse_mode='Markdown')

    elif query.data == 'temu':
        text = (
            "⚡ **صفقات Temu المجنونة:**\n\n"
            "🎁 هدايا للمستخدمين الجدد: [ضع رابطك هنا]\n"
            "📉 تخفيضات الفلاش 90%: [ضع رابطك هنا]\n\n"
            "استخدم الروابط أعلاه لتفعيل الخصم."
        )
        await query.edit_message_text(text=text, parse_mode='Markdown')

    elif query.data == 'alibaba':
        text = (
            "📦 **فرص Alibaba للجملة والدروبشيبينغ:**\n\n"
            "🌟 المنتجات الأكثر طلباً في 2026: [ضع رابطك هنا]\n"
            "🚛 موردين موثوقين (شحن سريع): [ضع رابطك هنا]"
        )
        await query.edit_message_text(text=text, parse_mode='Markdown')

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(handle_buttons))
    
    print("البوت الاحترافي يعمل الآن بنجاح...")
    application.run_polling()
