from customtkinter import *
from tkinter import *
import random
from tkinter import messagebox

win = CTk()
win.title('КНБ-25')
win.geometry('600x650+500+150')
win.resizable(0, 0)

game_list = ['камень', 'ножницы', 'бумага', 'огонь', 'вода', 'воздух', 'губка',
             'мужчина', 'волк', 'дьявол', 'пистолет', 'змея', 'дерево', 'дракон', 'молния',
             'динамит', 'ядер.оружие', 'пришелец', 'чаша', 'луна', 'таракан', 'женщина', 'обезьяна',
             'топор', 'солнце']
your_score = 0
bot_score = 0


def click():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[0]:
        messagebox.showinfo('-_-', 'У вас ничья!!!🗿')
    elif (ran_list == game_list[22] or ran_list == game_list[21] or ran_list == game_list[7]
          or ran_list == game_list[12] or ran_list == game_list[20] or ran_list == game_list[8]
          or ran_list == game_list[6] or ran_list == game_list[24] or ran_list == game_list[3]
          or ran_list == game_list[1] or ran_list == game_list[23] or ran_list == game_list[11]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score} 🗿')
        lbl3.configure(text=f'Ваш счёт:\n{your_score}')
    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота:\n{bot_score}')


def click1():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[1]:
        messagebox.showinfo('-_-', 'У вас ничья!!!✂️')
    elif (ran_list == game_list[20] or ran_list == game_list[8] or ran_list == game_list[6]
          or ran_list == game_list[2] or ran_list == game_list[19] or ran_list == game_list[5]
          or ran_list == game_list[23] or ran_list == game_list[11] or ran_list == game_list[22]
          or ran_list == game_list[21] or ran_list == game_list[7] or ran_list == game_list[12]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score} ✂️')
        lbl3.configure(text=f'Ваш счёт\n{your_score}')
    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота\n{bot_score}')


def click2():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[2]:
        messagebox.showinfo('-_-', 'У вас ничья!!!🧻')
    elif (ran_list == game_list[19] or ran_list == game_list[5] or ran_list == game_list[18]
          or ran_list == game_list[4] or ran_list == game_list[17] or ran_list == game_list[13]
          or ran_list == game_list[9] or ran_list == game_list[14] or ran_list == game_list[16]
          or ran_list == game_list[15] or ran_list == game_list[10] or ran_list == game_list[0]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score} 🧻')
        lbl3.configure(text=f'Ваш счёт\n{your_score}')
    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота\n{bot_score}')


def click3():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[3]:
        messagebox.showinfo('-_-', 'У вас ничья!!!🔥')
    elif (ran_list == game_list[1] or ran_list == game_list[23] or ran_list == game_list[11]
          or ran_list == game_list[22] or ran_list == game_list[21] or ran_list == game_list[7]
          or ran_list == game_list[12] or ran_list == game_list[20] or ran_list == game_list[8]
          or ran_list == game_list[6] or ran_list == game_list[2] or ran_list == game_list[13]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score} 🔥')
        lbl3.configure(text=f'Ваш счёт\n{your_score}')
    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота\n{bot_score}')


def click4():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[4]:
        messagebox.showinfo('-_-', 'У вас ничья!!!💧')
    elif (ran_list == game_list[17] or ran_list == game_list[13] or ran_list == game_list[9]
          or ran_list == game_list[14] or ran_list == game_list[16] or ran_list == game_list[15]
          or ran_list == game_list[10] or ran_list == game_list[0] or ran_list == game_list[24]
          or ran_list == game_list[1] or ran_list == game_list[3] or ran_list == game_list[23]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score} 💧')
        lbl3.configure(text=f'Ваш счёт\n{your_score}')

    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота\n{bot_score}')


def click5():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[5]:
        messagebox.showinfo('-_-', 'У вас ничья!!!🍃')
    elif (ran_list == game_list[18] or ran_list == game_list[4] or ran_list == game_list[17]
          or ran_list == game_list[13] or ran_list == game_list[9] or ran_list == game_list[14]
          or ran_list == game_list[16] or ran_list == game_list[15] or ran_list == game_list[10]
          or ran_list == game_list[0] or ran_list == game_list[24] or ran_list == game_list[3]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score} 🍃')
        lbl3.configure(text=f'Ваш счёт\n{your_score}')
    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота\n{bot_score}')


def click6():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[6]:
        messagebox.showinfo('-_-', 'У вас ничья!!!🧽')
    elif (ran_list == game_list[2] or ran_list == game_list[19] or ran_list == game_list[5]
          or ran_list == game_list[18] or ran_list == game_list[4] or ran_list == game_list[17]
          or ran_list == game_list[13] or ran_list == game_list[9] or ran_list == game_list[14]
          or ran_list == game_list[16] or ran_list == game_list[15] or ran_list == game_list[10]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score} 🧽')
        lbl3.configure(text=f'Ваш счёт\n{your_score}')
    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота\n{bot_score}')


def click7():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[7]:
        messagebox.showinfo('-_-', 'У вас ничья!!!👨')
    elif (ran_list == game_list[12] or ran_list == game_list[20] or ran_list == game_list[8]
          or ran_list == game_list[19] or ran_list == game_list[2] or ran_list == game_list[6]
          or ran_list == game_list[5] or ran_list == game_list[18] or ran_list == game_list[4]
          or ran_list == game_list[9] or ran_list == game_list[13] or ran_list == game_list[17]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score} 👨')
        lbl3.configure(text=f'Ваш счёт\n{your_score}')
    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота\n{bot_score}')


def click8():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[8]:
        messagebox.showinfo('-_-', 'У вас ничья!!!🐺')
    elif (ran_list == game_list[6] or ran_list == game_list[2] or ran_list == game_list[19]
          or ran_list == game_list[5] or ran_list == game_list[18] or ran_list == game_list[4]
          or ran_list == game_list[17] or ran_list == game_list[13] or ran_list == game_list[9]
          or ran_list == game_list[14] or ran_list == game_list[16] or ran_list == game_list[15]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score} 🐺')
        lbl3.configure(text=f'Ваш счёт\n{your_score}')
    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота\n{bot_score}')


def click9():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[9]:
        messagebox.showinfo('-_-', 'У вас ничья!!!👿')
    elif (ran_list == game_list[14] or ran_list == game_list[16] or ran_list == game_list[15]
          or ran_list == game_list[10] or ran_list == game_list[0] or ran_list == game_list[24]
          or ran_list == game_list[3] or ran_list == game_list[1] or ran_list == game_list[23]
          or ran_list == game_list[11] or ran_list == game_list[22] or ran_list == game_list[21]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score} 👿')
        lbl3.configure(text=f'Ваш счёт\n{your_score}')
    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота\n{bot_score}')


def click10():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[10]:
        messagebox.showinfo('-_-', 'У вас ничья!!!🔫')
    elif (ran_list == game_list[0] or ran_list == game_list[2] or ran_list == game_list[3]
          or ran_list == game_list[1] or ran_list == game_list[23] or ran_list == game_list[11]
          or ran_list == game_list[22] or ran_list == game_list[21] or ran_list == game_list[7]
          or ran_list == game_list[12] or ran_list == game_list[20] or ran_list == game_list[8]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score} 🔫')
        lbl3.configure(text=f'Ваш счёт\n{your_score}')
    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота\n{bot_score}')


def click11():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[11]:
        messagebox.showinfo('-_-', 'У вас ничья!!!🐍')
    elif (ran_list == game_list[22] or ran_list == game_list[21] or ran_list == game_list[7]
          or ran_list == game_list[12] or ran_list == game_list[20] or ran_list == game_list[8]
          or ran_list == game_list[6] or ran_list == game_list[2] or ran_list == game_list[19]
          or ran_list == game_list[5] or ran_list == game_list[18] or ran_list == game_list[4]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score} 🐍')
        lbl3.configure(text=f'Ваш счёт\n{your_score}')
    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота\n{bot_score}')


def click12():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[12]:
        messagebox.showinfo('-_-', 'У вас ничья!!!🌴')
    elif (ran_list == game_list[20] or ran_list == game_list[8] or ran_list == game_list[6]
          or ran_list == game_list[2] or ran_list == game_list[19] or ran_list == game_list[5]
          or ran_list == game_list[18] or ran_list == game_list[4] or ran_list == game_list[17]
          or ran_list == game_list[13] or ran_list == game_list[9] or ran_list == game_list[14]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score} 🌴')
        lbl3.configure(text=f'Ваш счёт\n{your_score}')
    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота\n{bot_score}')


def click13():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[13]:
        messagebox.showinfo('-_-', 'У вас ничья!!!🐉')
    elif (ran_list == game_list[9] or ran_list == game_list[14] or ran_list == game_list[16]
          or ran_list == game_list[15] or ran_list == game_list[10] or ran_list == game_list[0]
          or ran_list == game_list[24] or ran_list == game_list[3] or ran_list == game_list[1]
          or ran_list == game_list[23] or ran_list == game_list[11] or ran_list == game_list[22]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score} 🐉')
        lbl3.configure(text=f'Ваш счёт\n{your_score}')
    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота\n{bot_score}')


def click14():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[14]:
        messagebox.showinfo('-_-', 'У вас ничья!!!⚡')
    elif (ran_list == game_list[16] or ran_list == game_list[15] or ran_list == game_list[10]
          or ran_list == game_list[0] or ran_list == game_list[24] or ran_list == game_list[3]
          or ran_list == game_list[1] or ran_list == game_list[23] or ran_list == game_list[11]
          or ran_list == game_list[22] or ran_list == game_list[21] or ran_list == game_list[7]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score} ⚡')
        lbl3.configure(text=f'Ваш счёт\n{your_score}')
    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота\n{bot_score}')

def click15():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[15]:
        messagebox.showinfo('-_-', 'У вас ничья!!!🧨')
    elif (ran_list == game_list[10] or ran_list == game_list[0] or ran_list == game_list[24]
          or ran_list == game_list[3] or ran_list == game_list[1] or ran_list == game_list[23]
          or ran_list == game_list[11] or ran_list == game_list[22] or ran_list == game_list[21]
          or ran_list == game_list[7] or ran_list == game_list[12] or ran_list == game_list[20]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score} 🧨')
        lbl3.configure(text=f'Ваш счёт\n{your_score}')
    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота\n{bot_score}')

def click16():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[16]:
        messagebox.showinfo('-_-', 'У вас ничья!!!☢️')
    elif (ran_list == game_list[5] or ran_list == game_list[10] or ran_list == game_list[0]
          or ran_list == game_list[24] or ran_list == game_list[3] or ran_list == game_list[1]
          or ran_list == game_list[23] or ran_list == game_list[11] or ran_list == game_list[22]
          or ran_list == game_list[21] or ran_list == game_list[7] or ran_list == game_list[12]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score} ☢️')
        lbl3.configure(text=f'Ваш счёт\n{your_score}')
    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота\n{bot_score}')

def click17():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[17]:
        messagebox.showinfo('-_-', 'У вас ничья!!!👽')
    elif (ran_list == game_list[13] or ran_list == game_list[9] or ran_list == game_list[14]
          or ran_list == game_list[16] or ran_list == game_list[15] or ran_list == game_list[10]
          or ran_list == game_list[0] or ran_list == game_list[24] or ran_list == game_list[3]
          or ran_list == game_list[1] or ran_list == game_list[23] or ran_list == game_list[11]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score} 👽')
        lbl3.configure(text=f'Ваш счёт\n{your_score}')
    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота\n{bot_score}')

def click18():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[18]:
        messagebox.showinfo('-_-', 'У вас ничья!!!🍵')
    elif (ran_list == game_list[4] or ran_list == game_list[17] or ran_list == game_list[13]
          or ran_list == game_list[9] or ran_list == game_list[14] or ran_list == game_list[16]
          or ran_list == game_list[15] or ran_list == game_list[10] or ran_list == game_list[0]
          or ran_list == game_list[24] or ran_list == game_list[3] or ran_list == game_list[1]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score} 🍵')
        lbl3.configure(text=f'Ваш счёт\n{your_score}')
    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота\n{bot_score}')

def click19():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[19]:
        messagebox.showinfo('-_-', 'У вас ничья!!!🌙')
    elif (ran_list == game_list[5] or ran_list == game_list[18] or ran_list == game_list[4]
          or ran_list == game_list[17] or ran_list == game_list[13] or ran_list == game_list[9]
          or ran_list == game_list[14] or ran_list == game_list[16] or ran_list == game_list[15]
          or ran_list == game_list[10] or ran_list == game_list[0] or ran_list == game_list[24]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score}🌙')
        lbl3.configure(text=f'Ваш счёт\n{your_score}')
    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота\n{bot_score}')

def click20():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[20]:
        messagebox.showinfo('-_-', 'У вас ничья!!!🪳')
    elif (ran_list == game_list[8] or ran_list == game_list[6] or ran_list == game_list[2]
          or ran_list == game_list[19] or ran_list == game_list[5] or ran_list == game_list[18]
          or ran_list == game_list[4] or ran_list == game_list[17] or ran_list == game_list[13]
          or ran_list == game_list[9] or ran_list == game_list[14] or ran_list == game_list[16]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score} 🪳')
        lbl3.configure(text=f'Ваш счёт\n{your_score}')
    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота\n{bot_score}')

def click21():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[21]:
        messagebox.showinfo('-_-', 'У вас ничья!!!👱‍♀️')
    elif (ran_list == game_list[7] or ran_list == game_list[12] or ran_list == game_list[20]
          or ran_list == game_list[8] or ran_list == game_list[6] or ran_list == game_list[2]
          or ran_list == game_list[19] or ran_list == game_list[5] or ran_list == game_list[18]
          or ran_list == game_list[4] or ran_list == game_list[17] or ran_list == game_list[13]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score} 👱‍♀️')
        lbl3.configure(text=f'Ваш счёт\n{your_score}')
    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота\n{bot_score}')

def click22():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[22]:
        messagebox.showinfo('-_-', 'У вас ничья!!!🐒')
    elif (ran_list == game_list[21] or ran_list == game_list[7] or ran_list == game_list[12]
          or ran_list == game_list[20] or ran_list == game_list[8] or ran_list == game_list[6]
          or ran_list == game_list[2] or ran_list == game_list[19] or ran_list == game_list[5]
          or ran_list == game_list[18] or ran_list == game_list[4] or ran_list == game_list[17]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score}🐒')
        lbl3.configure(text=f'Ваш счёт\n{your_score}')
    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота\n{bot_score}')

def click23():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[23]:
        messagebox.showinfo('-_-', 'У вас ничья!!!🪓')
    elif (ran_list == game_list[22] or ran_list == game_list[21] or ran_list == game_list[7]
          or ran_list == game_list[12] or ran_list == game_list[20] or ran_list == game_list[8]
          or ran_list == game_list[6] or ran_list == game_list[2] or ran_list == game_list[19]
          or ran_list == game_list[5] or ran_list == game_list[18] or ran_list == game_list[11]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score} 🪓')
        lbl3.configure(text=f'Ваш счёт\n{your_score}')
    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота\n{bot_score}')

def click24():
    global your_score, bot_score
    ran_list = random.choice(game_list)
    lbl2.configure(text=ran_list)
    if ran_list == game_list[24]:
        messagebox.showinfo('-_-', 'У вас ничья!!!☀️')
    elif (ran_list == game_list[3] or ran_list == game_list[1] or ran_list == game_list[23]
          or ran_list == game_list[11] or ran_list == game_list[22] or ran_list == game_list[21]
          or ran_list == game_list[7] or ran_list == game_list[12] or ran_list == game_list[20]
          or ran_list == game_list[8] or ran_list == game_list[6] or ran_list == game_list[2]):
        your_score += 1
        messagebox.showinfo('Ура!!!', f'Вы выйграли!!!\nВаш счёт побед равен {your_score} ☀️')
        lbl3.configure(text=f'Ваш счёт\n{your_score}')
    else:
        bot_score += 1
        messagebox.showerror('О, нет!!!', f'Вы проиграли!!!\nCчёт побед бота равен {bot_score} 🤖')
        lbl4.configure(text=f'Счёт бота\n{bot_score}')

def reset_click():
    global your_score, bot_score
    your_score = 0
    bot_score = 0
    lbl3.configure(text=f'Ваш счёт\n{your_score}')
    lbl4.configure(text=f'Счёт бота\n{bot_score}')
    lbl2.configure(text='')


fram = CTkFrame(win, fg_color='#242424', height=450, width=480)
fram.pack()
btn = Button(fram, text='🗿', font=('Arial Bold', 50), fg='gray', bg='#242424', command=click,
             activebackground='#242424')
btn['border'] = '0'
btn.place(x=-40, y=0)
btn1 = Button(fram, text='✂️', font=('Arial Bold', 50), fg='silver', bg='#242424', command=click1,
              activebackground='#242424')
btn1['border'] = '0'
btn1.place(x=-30, y=100)
btn2 = Button(fram, text='🧻', font=('Arial Bold', 50), fg='white', bg='#242424', command=click2,
              activebackground='#242424')
btn2['border'] = '0'
btn2.place(x=-35, y=200)

btn3 = Button(fram, text='🔥', font=('Arial Bold', 50), fg='orange', bg='#242424', command=click3,
              activebackground='#242424')
btn3['border'] = '0'
btn3.place(x=100, y=0)

btn4 = Button(fram, text='💧', font=('Arial Bold', 50), fg='cyan', bg='#242424', command=click4,
              activebackground='#242424')
btn4['border'] = '0'
btn4.place(x=100, y=100)

btn5 = Button(fram, text='🍃', font=('Arial Bold', 50), fg='green', bg='#242424', command=click5,
              activebackground='#242424')
btn5['border'] = '0'
btn5.place(x=100, y=200)

btn6 = Button(fram, text='🧽', font=('Arial Bold', 50), fg='yellow', bg='#242424', command=click6,
              activebackground='#242424')
btn6['border'] = '0'
btn6.place(x=225, y=0)

btn7 = Button(fram, text='👨', font=('Arial Bold', 50), fg='#EBB998', bg='#242424', command=click7,
              activebackground='#242424')
btn7['border'] = '0'
btn7.place(x=225, y=100)

btn8 = Button(fram, text='🐺', font=('Arial Bold', 50), fg='GRAY', bg='#242424', command=click8,
              activebackground='#242424')
btn8['border'] = '0'
btn8.place(x=225, y=200)

btn9 = Button(fram, text='👿', font=('Arial Bold', 50), fg='purple', bg='#242424', command=click9,
              activebackground='#242424')
btn9['border'] = '0'
btn9.place(x=345, y=0)

btn10 = Button(fram, text='🔫', font=('Arial Bold', 50), fg='lime', bg='#242424', command=click10,
               activebackground='#242424')
btn10['border'] = '0'
btn10.place(x=345, y=100)

btn11 = Button(fram, text='🐍', font=('Arial Bold', 50), fg='#00ff7f', bg='#242424', command=click11,
               activebackground='#242424')
btn11['border'] = '0'
btn11.place(x=345, y=200)

btn12 = Button(fram, text='🌴', font=('Arial Bold', 50), fg='#3aa346', bg='#242424', command=click12,
               activebackground='#242424')
btn12['border'] = '0'
btn12.place(x=475, y=0)

btn13 = Button(fram, text='🐉', font=('Arial Bold', 50), fg='#06a397', bg='#242424', command=click13,
               activebackground='#242424')
btn13['border'] = '0'
btn13.place(x=475, y=100)

btn14 = Button(fram, text='⚡', font=('Arial Bold', 50), fg='#b2d3e6', bg='#242424', command=click14,
               activebackground='#242424')
btn14['border'] = '0'
btn14.place(x=475, y=200)

btn15 = Button(fram, text='🧨', font=('Arial Bold', 50), fg='red', bg='#242424', command=click15,
               activebackground='#242424')
btn15['border'] = '0'
btn15.place(x=-40, y=300)

btn16 = Button(fram, text='☢️', font=('Arial Bold', 50), fg='#d3dd18', bg='#242424', command=click16,
               activebackground='#242424')
btn16['border'] = '0'
btn16.place(x=100, y=300)

btn17 = Button(fram, text='👽', font=('Arial Bold', 50), fg='#42bd41', bg='#242424', command=click17,
               activebackground='#242424')
btn17['border'] = '0'
btn17.place(x=225, y=300)

btn18 = Button(fram, text='🍵', font=('Arial Bold', 50), fg='#eeeeee', bg='#242424', command=click18,
               activebackground='#242424')
btn18['border'] = '0'
btn18.place(x=350, y=300)

btn19 = Button(fram, text='🌙', font=('Arial Bold', 50), fg='#80d0ff', bg='#242424', command=click19,
               activebackground='#242424')
btn19['border'] = '0'
btn19.place(x=475, y=300)

btn20 = Button(fram, text='🪳', font=('Arial Bold', 50), fg='#be7656', bg='#242424', command=click20,
               activebackground='#242424')
btn20['border'] = '0'
btn20.place(x=-40, y=400)

btn21 = Button(fram, text='👱‍', font=('Arial Bold', 50), fg='#EBB998', bg='#242424', command=click21,
               activebackground='#242424')
btn21['border'] = '0'
btn21.place(x=100, y=400)

btn22 = Button(fram, text='🐒', font=('Arial Bold', 50), fg='#895b4a', bg='#242424', command=click22,
               activebackground='#242424')
btn22['border'] = '0'
btn22.place(x=225, y=400)

btn23 = Button(fram, text='🪓', font=('Arial Bold', 50), fg='#c62828', bg='#242424', command=click23,
               activebackground='#242424')
btn23['border'] = '0'
btn23.place(x=350, y=400)

btn24 = Button(fram, text='☀️', font=('Arial Bold', 50), fg='#effd5f', bg='#242424', command=click24,
               activebackground='#242424')
btn24['border'] = '0'
btn24.place(x=475, y=400)

lbl3 = CTkLabel(win, text=f'Ваш счёт:\n{your_score}', font=('arial', 25), fg_color='#242424', text_color='white')
lbl3.pack(side=LEFT)
lbl4 = CTkLabel(win, text=f'Счёт бота:\n{bot_score}', font=('arial', 25), fg_color='#242424', text_color='white')
lbl4.pack(side=RIGHT)

lbl = CTkLabel(win, text='🤖', font=('arial', 60), fg_color='#242424', text_color='silver')
lbl.pack()
lbl2 = CTkLabel(win, text='', font=('arial', 30), fg_color='#f5fffa', text_color='black', width=250,
                height=40)
lbl2.pack()
res_but = Button(win, text='Сбросить', font=('Arial Bold', 35), fg='white', bg='#242424', command=reset_click,
                 activebackground='#242424')
res_but['border'] = '0'
res_but.place(x=250, y=700)
win.mainloop()
