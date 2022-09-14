from pyrogram import Client, filters
import os,sys,threading
api_id = 000
api_hash = "XXX"
app = Client("my_account", api_id=api_id, api_hash=api_hash)
if "linux" in sys.platform:
    os.system("clear")
elif sys.platform == "win32":
    os.system("cls")
print("Spam bot By Phelete started.")
class data:
    text=""
    iter=0
    thread=1
    brk=0
def reset_data():
    data.text=""
    data.iter=0
    data.thread=1
    data.brk=0
def spam(id, iter, text, thead):
    if iter == 0:
        while 1:
            if data.brk:
                break
            app.send_message(id, text)
    else:
        for i in range(round(int(iter)/int(thead))):
            if data.brk:
                break
            app.send_message(id, text)
@app.on_message(filters.command('settext')&filters.me)
def settext(client, message):
    app.delete_messages(message.chat.id, message.id)
    lei=len(message.command)
    if lei > 1:
        a=""
        for i in range(1,lei):
            a+=message.command[i]+" "
        data.text=a
        app.send_message(message.chat.id, f"Успешно, текст: {data.text}")
    else:
        app.send_message(message.chat.id, "Введите текст\nПример: /settext Спам")
@app.on_message(filters.command('setiter')&filters.me)
def setiter(client, message):
    app.delete_messages(message.chat.id, message.id)
    lei=len(message.command)
    if lei > 1:
        data.iter=message.command[1]
        app.send_message(message.chat.id, f"Успешно, колличество сообщений: {data.iter}")
    else:
        app.send_message(message.chat.id, "Введите колличество сообщений, 0-Бесконечно\nПример: /setiter 10")
@app.on_message(filters.command('setthread')&filters.me)
def setthread(client, message):
    app.delete_messages(message.chat.id, message.id)
    lei=len(message.command)
    if lei > 1:
        if int(message.command[1])>=1:
            data.thread=message.command[1]
            app.send_message(message.chat.id, f"Успешно, колличество потоков: {data.thread}")
        else:
            app.send_message(message.chat.id, f"Колличество потоков должно быть больше 0.")
    else:
        app.send_message(message.chat.id, "Введите колличество потоков\nПример: /setthread 3")
@app.on_message(filters.command('help')&filters.me)
def help(client, message):
    app.delete_messages(message.chat.id, message.id)
    app.send_message(message.chat.id, "/settext-Установить текст спама(Писать себе в ЛС)\n/setiter-Установить колличество сообщений(Писать себе в ЛС)\n/setthread-Установить колличество потоков(Писать себе в ЛС)\n/spam-Начать спам(Писать в ЛС жертве\n\n/text-Посмотреть установленный текст(Писать себе в ЛС)\n/iter-Посмотреть колличество сообщений(Писать себе в ЛС)\n/thread-Посмотреть колличество потоков(Писать себе в ЛС)\n\nMade by Phelete with Love❤️")
@app.on_message(filters.command('text')&filters.me)
def text(client, message):
    app.delete_messages(message.chat.id, message.id)
    if data.text:
        app.send_message(message.chat.id, f"Ваш текст: {data.text}")
    else:
        app.send_message(message.chat.id, "Текст еще не установлен, напишите '/settext Ваш текст' для его установки.")
@app.on_message(filters.command('iter')&filters.me)
def iter(client, message):
    iter=str(data.iter)
    if iter == "0":
        iter=iter.replace("0", "Бесконечно")
    app.delete_messages(message.chat.id, message.id)
    app.send_message(message.chat.id, f"Колличество сообщений: {iter}")
@app.on_message(filters.command("thread")&filters.me)
def thread(client,message):
    app.delete_messages(message.chat.id, message.id)
    app.send_message(message.chat.id, f"Колличество потоков: {data.thread}")
@app.on_message(filters.command('stop'))
def stop(client, message):
    app.delete_messages(message.chat.id, message.id)
    data.brk=1
@app.on_message(filters.command('spam'))
def main(client, message):
    app.delete_messages(message.chat.id, message.id)
    text=data.text
    thread=data.thread
    iter=data.iter
    if text:
        for i in range(int(data.thread)):
            threading.Thread(target=spam, args=(message.chat.id,iter,text,thread)).start()
    else:
        app.send_message("me", "Неверный текст напишите /help и настройте спам.")
    reset_data()
app.run()