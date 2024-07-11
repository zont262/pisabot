import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from datetime import datetime

from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import  Router
import sqlite3

from aiogram.filters.chat_member_updated import \
    ChatMemberUpdatedFilter, IS_NOT_MEMBER, MEMBER, ADMINISTRATOR
from aiogram.types import ChatMemberUpdated
import random
import time
import  config_group



start = time.time()
promocode = True

router = Router()


db = sqlite3.connect('user.db')
sql = db.cursor()

global secods
global minutes
global has
global day
global mes
global start_time

countss = 0
adminPassword = 0

colum = [    'id',     'pisa',      'GodPisa',  'MesacPisa', 'DataPisa', 'Podkrytka']
columTip = [ 'BIGINT',  'BIGINT',   'INT',      'INT',       'INT',        'INT']
start_time = time.time()



sql.execute("""CREATE TABLE IF NOT EXISTS users (
id BIGINT,
pisa BIGINT,
GodPisa INT,
MesacPisa INT,
DataPisa INT,
Podkrytka INT
)""")

db.commit()
db.close()










# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7314933896:AAEJgEiRdVnvLzUi5w0BE2Q604I98S9IJ0o")
# Диспетчер
dp = Dispatcher()
dp.include_router(router)
dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")

vklbot = time.time()

adminPassword = random.randint(0, 999999)
print("адммин пароль " + str(adminPassword))


def newPass():
    adminPassword = random.randint(0, 999999)
    print("адммин пароль " + str(adminPassword))






# Хэндлер на команду /start
@dp.message(Command("registration"))
async def cmd_start(message: types.Message):
    db = sqlite3.connect(f'{message.chat.id}.pisa.db')
    sql = db.cursor()
    sql.execute(f'SELECT id FROM users WHERE id == {message.from_user.id}')
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES ({message.from_user.id},{0}, {2023}, {1}, {1}, {0})")
        db.commit()
        db.close()
        await message.answer("Спасибо за регистрацию!")
    else:
        await message.answer("ВЫ УЖЕ ЗАРЕГИСТРИРОВАНЫ")








@dp.message(Command("dick"))
async def cmd_reply(message: types.Message):
    db = sqlite3.connect(f'{message.chat.id}.pisa.db')
    sql = db.cursor()

    sql.execute(f'SELECT id FROM users WHERE id == {message.from_user.id}')
    if sql.fetchone() is None:
        await message.reply('сначала надо зарегистрироваться \n/registration')
    else:

        sql.execute(f'SELECT GodPisa FROM users WHERE id = {message.from_user.id}')
        god = sql.fetchone()
        sql.execute(f'SELECT MesacPisa FROM users WHERE id = {message.from_user.id}')
        mesac = sql.fetchone()
        sql.execute(f'SELECT DataPisa FROM users WHERE id = {message.from_user.id}')
        data = sql.fetchone()
        sql.execute(f'SELECT pisa FROM users WHERE id = {message.from_user.id}')
        pisa = sql.fetchone()

        print(pisa)
        for god in god:
            for mesac in mesac:
                for data in data:
                    for pisa in pisa:
                        if god == None:
                            god = int(datetime.now().strftime("%Y"))
                            god -= 1
                        if int(god) < int(datetime.now().strftime("%Y")):
                            pisa2 = random.randint(-10, 10)
                            pisa += pisa2
                            await message.reply('выпало число ' + str(pisa2) + "\nобщий размер: " + str(pisa))
                            sql.execute(f'UPDATE users SET pisa = {pisa} WHERE id = {message.from_user.id}')
                            sql.execute(f'UPDATE users SET GodPisa = {int(datetime.now().strftime("%Y"))} WHERE id = {message.from_user.id}')
                            sql.execute(f'UPDATE users SET MesacPisa = {int(datetime.now().strftime("%m"))} WHERE id = {message.from_user.id}')
                            sql.execute(f'UPDATE users SET DataPisa = {int(datetime.now().strftime("%d"))} WHERE id = {message.from_user.id}')
                            db.commit()
                            db.close()
                            return
                        else:
                            if mesac == None:
                                mesac = int(datetime.now().strftime("%m"))
                                mesac -= 1
                            if int(mesac) < int(datetime.now().strftime("%m")):
                                pisa2 = random.randint(-10, 10)
                                pisa += pisa2
                                await message.reply('выпало число ' + str(pisa2) + "\nобщий размер: " + str(pisa))
                                sql.execute(f'UPDATE users SET pisa = {pisa} WHERE id = {message.from_user.id}')
                                sql.execute(f'UPDATE users SET GodPisa = {int(datetime.now().strftime("%Y"))} WHERE id = {message.from_user.id}')
                                sql.execute(f'UPDATE users SET MesacPisa = {int(datetime.now().strftime("%m"))} WHERE id = {message.from_user.id}')
                                sql.execute(f'UPDATE users SET DataPisa = {int(datetime.now().strftime("%d"))} WHERE id = {message.from_user.id}')
                                db.commit()
                                db.close()
                                return
                            else:
                                if data == None:
                                    data = int(datetime.now().strftime("%d"))
                                    data -= 1
                                if int(data) < int(datetime.now().strftime("%d")):
                                    pisa2 = random.randint(-10, 10)
                                    pisa += pisa2
                                    await message.reply('выпало число ' + str(pisa2) + "\nобщий размер: " + str(pisa))
                                    sql.execute(f'UPDATE users SET pisa = {pisa} WHERE id = {message.from_user.id}')
                                    sql.execute(f'UPDATE users SET GodPisa = {int(datetime.now().strftime("%Y"))} WHERE id = {message.from_user.id}')
                                    sql.execute(f'UPDATE users SET MesacPisa = {int(datetime.now().strftime("%m"))} WHERE id = {message.from_user.id}')
                                    sql.execute(f'UPDATE users SET DataPisa = {int(datetime.now().strftime("%d"))} WHERE id = {message.from_user.id}')
                                    db.commit()
                                    db.close()
                                    return
                                else:
                                    await message.reply("Вы уже играли сегодня! Попробуйте завтра")













@dp.message(Command("бд"))

async def cmd_reply(message: types.Message):
    db = sqlite3.connect(f'{message.chat.id}.pisa.db')
    sql = db.cursor()
    column_tip = 0

    # Проверяем наличие каждого столбца в таблице
    for column_name in colum:
        try:
    # Проверяем, существует ли столбец

            sql.execute("PRAGMA table_info(users)").fetchall()
            if column_name not in [i[1] for i in sql.fetchall()]:

                column_tip += 1
                sql.execute(f"ALTER TABLE users ADD COLUMN {column_name} {columTip[column_tip - 1]}")
                db.commit()

            else:
                column_tip += 1
                print(column_tip)
        except:
            continue



@dp.message(Command("toppisa2"))
async def cmd_reply(message: types.Message):
    top = [-1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000]
    text2 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    i = 0
    db = sqlite3.connect(f'{message.chat.id}.pisa.db')
    sql = db.cursor()
    sql.execute("SELECT pisa FROM users")
    rows = sql.fetchall()


    for row in rows:

        for row in row:
            if row != -9999:
                if row != None:
                        top[i] = row
                        i += 1

        top.sort(reverse=True)
        massivImen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(0, len(top)):
            sql.execute(f'SELECT COUNT(id) FROM users WHERE pisa = {top[i]}')
            countId = sql.fetchone()
            for countId in countId:
                if int(countId) < 2:
                    sql.execute(f'SELECT id FROM users WHERE pisa = {top[i]}')
                    idFind = sql.fetchone()
                    if idFind != None:
                        for idFind in idFind:
                            massivImen[i] = idFind
                            UserInfo = await bot.get_chat_member(message.chat.id, int(idFind))
                            text2[i] = str(i) + str(') ') + str(UserInfo.user.first_name) + ": " + str(top[i]) + str(" см")
                            continue
                else:
                    if countId == 2:
                        sql.execute(f'SELECT id FROM users WHERE pisa = {top[i]} LIMIT 1 OFFSET {0}')
                        idFind = sql.fetchone()
                        if idFind != None:
                            for idFind in idFind:
                                massivImen[i] = idFind
                                UserInfo = await bot.get_chat_member(message.chat.id, int(idFind))
                                text2[i] = str(i) + str(') ') + str(UserInfo.user.first_name) + ": " + str(top[i]) + str(" см")
                                continue

                        sql.execute(f'SELECT id FROM users WHERE pisa = {top[i]} LIMIT 1 OFFSET {1}')
                        idFind = sql.fetchone()
                        if idFind != None:
                            for idFind in idFind:
                                massivImen[i] = idFind
                                UserInfo = await bot.get_chat_member(message.chat.id, int(idFind))
                                text2[i] = str(i) + str(') ') + str(UserInfo.user.first_name) + ": " + str(
                                    top[i]) + str(" см")
                                continue

                        if countId == 3:
                            sql.execute(f'SELECT id FROM users WHERE pisa = {top[i]} LIMIT 1 OFFSET {0}')
                            idFind = sql.fetchone()
                            if idFind != None:
                                for idFind in idFind:
                                    massivImen[i] = idFind
                                    UserInfo = await bot.get_chat_member(message.chat.id, int(idFind))
                                    text2[i] = str(i) + str(') ') + str(UserInfo.user.first_name) + ": " + str(
                                        top[i]) + str(" см")
                                    continue

                            sql.execute(f'SELECT id FROM users WHERE pisa = {top[i]} LIMIT 1 OFFSET {1}')
                            idFind = sql.fetchone()
                            if idFind != None:
                                for idFind in idFind:
                                    massivImen[i] = idFind
                                    UserInfo = await bot.get_chat_member(message.chat.id, int(idFind))
                                    text2[i] = str(i) + str(') ') + str(UserInfo.user.first_name) + ": " + str(
                                        top[i]) + str(" см")
                                    continue

                            sql.execute(f'SELECT id FROM users WHERE pisa = {top[i]} LIMIT 1 OFFSET {2}')
                            idFind = sql.fetchone()
                            if idFind != None:
                                for idFind in idFind:
                                    massivImen[i] = idFind
                                    UserInfo = await bot.get_chat_member(message.chat.id, int(idFind))
                                    text2[i] = str(i) + str(') ') + str(UserInfo.user.first_name) + ": " + str(
                                        top[i]) + str(" см")
                                    continue

                            if countId == 4:
                                sql.execute(f'SELECT id FROM users WHERE pisa = {top[i]} LIMIT 1 OFFSET {0}')
                                idFind = sql.fetchone()
                                if idFind != None:
                                    for idFind in idFind:
                                        massivImen[i] = idFind
                                        UserInfo = await bot.get_chat_member(message.chat.id, int(idFind))
                                        text2[i] = str(i) + str(') ') + str(UserInfo.user.first_name) + ": " + str(
                                            top[i]) + str(" см")
                                        continue

                                sql.execute(f'SELECT id FROM users WHERE pisa = {top[i]} LIMIT 1 OFFSET {1}')
                                idFind = sql.fetchone()
                                if idFind != None:
                                    for idFind in idFind:
                                        massivImen[i] = idFind
                                        UserInfo = await bot.get_chat_member(message.chat.id, int(idFind))
                                        text2[i] = str(i) + str(') ') + str(UserInfo.user.first_name) + ": " + str(
                                            top[i]) + str(" см")
                                        continue

                                sql.execute(f'SELECT id FROM users WHERE pisa = {top[i]} LIMIT 1 OFFSET {2}')
                                idFind = sql.fetchone()
                                if idFind != None:
                                    for idFind in idFind:
                                        massivImen[i] = idFind
                                        UserInfo = await bot.get_chat_member(message.chat.id, int(idFind))
                                        text2[i] = str(i) + str(') ') + str(UserInfo.user.first_name) + ": " + str(
                                            top[i]) + str(" см")
                                        continue
                                sql.execute(f'SELECT id FROM users WHERE pisa = {top[i]} LIMIT 1 OFFSET {3}')
                                idFind = sql.fetchone()
                                if idFind != None:
                                    for idFind in idFind:
                                        massivImen[i] = idFind
                                        UserInfo = await bot.get_chat_member(message.chat.id, int(idFind))
                                        text2[i] = str(i) + str(') ') + str(UserInfo.user.first_name) + ": " + str(
                                            top[i]) + str(" см")
                                        continue

    await message.answer(f'' + "топ игроков\n" +  str(text2[0]) + "\n" + str(text2[1]) + "\n" + str(text2[2]) + "\n" + str(text2[3]) + "\n" + str(text2[4])+ "\n" + str(text2[5]) + "\n" + str(text2[6]) + "\n" + str(text2[7])+ "\n" + str(text2[8]) + "\n" + str(text2[9]))
    db.close()

@dp.message(F.text)
async def echo_with_time(message: Message):
    if message.text.lower().split()[0] == "выдать":
        if message.text.lower().split()[1] == "pisa":

            db = sqlite3.connect(f'{message.chat.id}.pisa.db')
            sql = db.cursor()
            sql.execute(f'SELECT id FROM users WHERE id == {message.from_user.id}')
            if sql.fetchone() is None:
                await message.reply('сначала надо зарегистрироваться \n/registration')
            else:

                if message.text.lower().split()[2] == str(adminPassword):
                        print(123)
                        name1 = message.from_user.username
                        sql.execute(f'SELECT pisa FROM users WHERE id = {message.text.lower().split()[3]}')
                        pisa = sql.fetchone()
                        for pisa in pisa:
                            newBalance = pisa + int(message.text.lower().split()[4])
                            sql.execute(f'UPDATE users SET pisa = {newBalance} WHERE id = {message.text.lower().split()[3]}')
                            db.commit()
                            db.close()

                            UserInfo = await bot.get_chat_member(message.chat.id,int(message.text.lower().split()[3]))
                            if UserInfo.user.username != None:

                                await  message.answer(f"администратор @{name1} успешно выдал пользователю @{UserInfo.user.username} {message.text.lower().split()[4]} см")
                                return
                            else:
                                await  message.answer(f"администратор @{name1} успешно выдал пользователю {message.text.lower().split()[2]} {message.text.lower().split()[4]} см")
                                return
                        return




    if message.text.lower().split()[0] == "админка":
        db = sqlite3.connect(f'{message.chat.id}.pisa.db')
        sql = db.cursor()
        sql.execute(f'SELECT idd FROM users WHERE idd == {message.from_user.id}')
        if sql.fetchone() is None:
            await message.reply('сначала надо зарегистрироваться \n/registration')
        else:
            if message.text.lower().split()[1] == str(adminPassword):
                sql.execute(f'SELECT adminLvlBot FROM users WHERE idd = {message.from_user.id}')
                MyLvl = sql.fetchone()
                for MyLvl in MyLvl:
                    MyLvl = int(5)
                    sql.execute(f'UPDATE users SET adminLvlBot = {MyLvl} WHERE idd = {message.from_user.id}')
                    db.commit()
                    db.close()
                    newPass()
                    await  message.answer(f'пароль верный')
            else:
                await  message.answer(f'пароль неверный')




    if message.text.lower().split()[0] == ".ид":
        if message.reply_to_message:
            UserInfo = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)

        else:
            UserInfo = await bot.get_chat_member(message.chat.id, message.from_user.id)
        UserInfo = UserInfo.user.id
        await  message.answer(f"id равен {UserInfo}")

    










router.my_chat_member.filter(F.chat.type.in_({"group", "supergroup"}))

chats_variants = {
    "group": "группу",
    "supergroup": "супергруппу"
}


# Не удалось воспроизвести случай добавления бота как Restricted,
# поэтому примера с ним не будет


@router.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=IS_NOT_MEMBER >> ADMINISTRATOR
    )
)
async def bot_added_as_admin(event: ChatMemberUpdated):
    # Самый простой случай: бот добавлен как админ.
    # Легко можем отправить сообщение
    await event.answer(
        text=f"Привет! Спасибо, что добавили меня в "
             f'{chats_variants[event.chat.type]} "{event.chat.title}" '
             f"как администратора. ID чата: {event.chat.id}"
    )
    db = sqlite3.connect(f'{event.chat.id}.pisa.db')
    sql = db.cursor()

    sql.execute("""CREATE TABLE IF NOT EXISTS users (
    id BIGINT,
    pisa BIGINT,
    GodPisa INT,
    MesacPisa INT,
    DataPisa INT,
    Podkrytka INT
    )""")

    db.commit()
    db.close()
    config_group.newBD(event.chat.id)



@router.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=IS_NOT_MEMBER >> MEMBER
    )
)
async def bot_added_as_member(event: ChatMemberUpdated):
    # Вариант посложнее: бота добавили как обычного участника.
    # Но может отсутствовать право написания сообщений, поэтому заранее проверим.
    chat_info = await bot.get_chat(event.chat.id)
    if chat_info.permissions.can_send_messages:
        await event.answer(
            text=f"Привет! Спасибо, что добавили меня в "
                 f'{chats_variants[event.chat.type]} "{event.chat.title}" '
                 f"как обычного участника. ID чата: {event.chat.id}"
        )
        db = sqlite3.connect(f'{event.chat.id}.pisa.db')
        sql = db.cursor()

        sql.execute("""CREATE TABLE IF NOT EXISTS users (
           id BIGINT,
           pisa BIGINT,
           GodPisa INT,
           MesacPisa INT,
           DataPisa INT,
           Podkrytka INT
           )""")

        db.commit()
        db.close()
        config_group.newBD(event.chat.id)

    else:
        print("Как-нибудь логируем эту ситуацию")



async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())
