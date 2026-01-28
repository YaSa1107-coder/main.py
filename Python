import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# إعداد السجلات (Logs) لمعرفة ما إذا كان البوت يعمل أو يواجه أخطاء
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# جلب التوكن من إعدادات Render (Environment Variables)
TOKEN = os.getenv('BOT_TOKEN')

# الدالة التي تعمل عند كتابة أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    welcome_msg = (
        f"أهلاً بك يا {user_name} في بوتك الأول! 🚀\n\n"
        "أنا أعمل الآن من خلال سيرفرات Render.\n"
        "يمكنك الآن البدء بتطويري لإضافة ميزات الربح."
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_msg)

# الدالة التي تعمل عند كتابة أمر /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="هذا البوت قيد التطوير لتحقيق الربح!")

if __name__ == '__main__':
    # بناء البوت باستخدام التوكن
    if not TOKEN:
        print("خطأ: لم يتم العثور على BOT_TOKEN في إعدادات البيئة!")
    else:
        application = ApplicationBuilder().token(TOKEN).build()
        
        # إضافة الأوامر للبوت
        start_handler = CommandHandler('start', start)
        help_handler = CommandHandler('help', help_command)
        
        application.add_handler(start_handler)
        application.add_handler(help_handler)
        
        print("البوت انطلق بنجاح...")
        application.run_polling()
