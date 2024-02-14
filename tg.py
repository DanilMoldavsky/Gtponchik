from gpt.gpt import Gpt
from db.sqlite import SQLite
import telebot

bot = telebot.TeleBot('YOUR_TOKEN')
gpt = Gpt()
MEMORY = True



@bot.message_handler(commands=['start'])
def start_message(message):
    
    bot.send_message(message.chat.id, '''👋 Привет!
💎 С помощью этого бота ты сможешь общаться с чатом *Gpt4*! Бот сохраняет историю диалогов и gpt может вести диалог 🗣
📲 Чтобы начать просто пришли любой текст не длиннее `4700` символов ✏
                     ''', parse_mode="Markdown")


@bot.message_handler(commands=['myid'])
def send_id(message):
    bot.send_message(message.from_user.id, f'{message.from_user.id}')


@bot.message_handler(commands=['memory'])
def memory_command(message):
    global MEMORY
    MEMORY = not MEMORY
    bot.reply_to(message, "Memory enabled" if MEMORY == True else "Memory disabled")



@bot.message_handler(content_types=['text'])
def get_user_text(message):
    try:
        global gpt
        
        
        gpt.prompts = message.text


        response = gpt.talk_valid_markdown(prompts=gpt.prompts)
        bot.send_message(message.from_user.id, response, parse_mode="Markdown")
        
        
        
            
    except Exception as e:
        print(e)
        with open('log_tg.txt', 'a', encoding="utf-8") as file:
            file.write(f'\n{str(e)}')
        bot.send_message(message.from_user.id,  '''Простите, сейчас мой создатель меня дорабатывает, попробуйте позже 
        Если проблема *долго* не решается напишите нашему создателю *@Sad_Manners*
                         ''', parse_mode="Markdown")


if __name__ == '__main__':
    bot.polling(none_stop=True)
