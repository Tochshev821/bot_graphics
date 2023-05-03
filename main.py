#btoken = '5888951302:AAHxZ4Vj92fQJClD7HVmvDCQjSkUE5waisI'
import telebot
import numpy as np
import matplotlib.pyplot as plt
import math
import datetime

class Error(Exception):
    """Базовый класс для других исключений"""
    pass
class ValueNorNumber(Error):
    """вызываем при отправки не числа"""
    pass


btoken = '5888951302:AAHxZ4Vj92fQJClD7HVmvDCQjSkUE5waisI'
bot = telebot.TeleBot(btoken)

plt.switch_backend('Agg')
numplot = 1



def funcg(x):
    try:
        return 1/x
    except ZeroDivisionError:
        return 0

def plotgiper(yy):
    global numplot
    y = []
    px = []
    x = range (-1*yy, 0)
    for r in x:
        y.append(funcg(r))
        px.append(r)

    plt.gca().spines["left"].set_position("zero")
    plt.gca().spines["bottom"].set_position("zero")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

    plt.plot(px, y, color="red", marker="o")

    y=[]
    px = []
    x = range(1,yy+1)
    for r in x:
        y.append(funcg(r))
        px.append(r)
    plt.plot(px, y, color="blue", marker="o")

    filename = 'giper_' + str(numplot) + '.png'
    plt.savefig(filename)
    plt.close()
    numplot+=1
    return filename

class Graphic(object):
    def funcg(x):
        try:
            return 1 / x
        except ZeroDivisionError:
            return 0

    #все методы экземпляра ожидают первого аргумента, который по обычаю мы называем self
    def plotgiper(self,yy):
        global numplot
        y = []
        px = []
        x = range(-1 * yy, 0)
        for r in x:
            y.append(funcg(r))
            px.append(r)

        plt.gca().spines["left"].set_position("zero")
        plt.gca().spines["bottom"].set_position("zero")
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)

        plt.plot(px, y, color="red", marker="o")

        y = []
        px = []
        x = range(1, yy + 1)
        for r in x:
            y.append(funcg(r))
            px.append(r)
        plt.plot(px, y, color="blue", marker="o")

        filename = 'giper_' + str(numplot) + '.png'
        plt.savefig(filename)
        plt.close()
        numplot += 1
        return filename


@bot.message_handler(commands=['graphic'])
def get_graph(message):
    bot.send_message(message.chat.id, 'Сколько точек использовать?')
    bot.register_next_step_handler(message, send_graphic)


@bot.message_handler(commands=['cat'])
def send_random_cat(message):
    url = 'https://cataas.com/cat?t=' + str(datetime.datetime.now())
    bot.send_photo(message.chat.id, url)


@bot.message_handler(content_types=['text'])
def send_graphic(message):
    try:
        graph = Graphic()
        if message.text.isdigit():
            graphicname = graph.plotgiper(int(message.text))
            gr = open(graphicname, 'rb')
            bot.send_photo(message.chat.id, gr)
        else:
            raise ValueNorNumber
    except ValueNorNumber:
        print("NE CHISLO")
        bot.send_message(message.chat.id, 'Не число')







if __name__ == '__main__':
    bot.infinity_polling()

