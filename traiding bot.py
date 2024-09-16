import telebot
import schedule
import time
from tradingview_ta import TA_Handler, Interval, Exchange


def parsing_kline_1(): # парсинг часовых свечей
    for i in range(5):
        try:
            output = TA_Handler(symbol='GBPUSD',
                                screener='forex',
                                exchange='FX_IDC',
                                interval=Interval.INTERVAL_1_HOUR)
            result = output.get_analysis().indicators
            return result
        except:
            pass


def parsing_kline_4(): # парсинг четырех часовых свечей
    for i in range(5):
        try:
            output = TA_Handler(symbol='GBPUSD',
                                screener='forex',
                                exchange='FX_IDC',
                                interval=Interval.INTERVAL_4_HOURS)
            result = output.get_analysis().indicators
            return result
        except:
            pass


def calculations(result): # расчет свечи
    if result['open'] >= result['close']:
        line_1 = result['high'] - result['open']
        line_2 = result['open'] - result['close']
        line_3 = result['close'] - result['low']
    else:
        line_1 = result['high'] - result['close']
        line_2 = result['close'] - result['open']
        line_3 = result['open'] - result['low']
    return [line_1, line_2, line_3]


bot = telebot.TeleBot('7124348873:AAEgaQPOFWFgZLqXQYETUbLH62Rd8r19zUA')
chat_id = '932619568'


def result_calculate_1(): # проверка на удовлетворение условий по стратегии часовых свечей
    list_result = calculations(parsing_kline_1())
    if (list_result[0] + list_result[1]) * 2 <= list_result[2]:
        send_message_1()
    elif (list_result[1] + list_result[2]) * 2 <= list_result[0]:
        send_message_1()


def result_calculate_4(): # проверка на удовлетворение условий по стратегии четырех часовых свечей
    list_result = calculations(parsing_kline_4())
    if (list_result[0] + list_result[1]) * 2 <= list_result[2]:
        send_message_1()
    elif (list_result[1] + list_result[2]) * 2 <= list_result[0]:
        send_message_1()


def send_message_1(): # отправка сообщений в телеграмм на наличие часовой свечи
    message = 'Есть часовая свеча'
    bot.send_message(chat_id=chat_id, text=message)


def send_message_4(): # отправка сообщений в телеграмм на наличие четырех часовой свечи
    message = 'Есть 4ёх часовая свеча'
    bot.send_message(chat_id=chat_id, text=message)


# Задаем время начала исполнения скрипта
schedule.every().hour.at('59:55').do(result_calculate_1)
schedule.every(4).hours.at('59:55').do(result_calculate_4)

# Бесконечный цикл для проверки расписания
while True:
    schedule.run_pending()
