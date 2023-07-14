import telebot
from glob import glob
from telebot import types 
from bs4 import BeautifulSoup as BS 

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from get_online import get_list_movie_online
from get_online import get_movie_online

from download_film import get_list_film_download
from download_film import get_film_download

from download_series import get_list_series_download
from download_series import get_series_download  
from download_series import get_list_of_ser_download

bot = telebot.TeleBot('YOUR API') 

global list_movie, list_number, list_series, full_name
list_movie = {}
list_number = {}
list_series = {}
full_name = ''

#start
@bot.message_handler(commands = ['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
    item1 = types.KeyboardButton("Смотреть онлайн")
    item2 = types.KeyboardButton("Скачать mp4")
    markup.add(item1, item2)
    photo = open('welcome.png', 'rb')
    bot.send_photo(message.chat.id, photo, "Добро пожаловать, " + message.from_user.first_name + "! 🥳\n"
                     "Чтобы приступить к просмотру фильмов и серилов\n"
                     "воспользуйтесь кнопками снизу 👇\n"
                     "Приятного просмотра!🍿", reply_markup = markup)
    
# клавиатура reply
@bot.message_handler(content_types = ['text'])
def movie_start(message):
    global prev_message
    global prev_id
    
    if message.chat.type == 'private':
        if message.text == 'Смотреть онлайн':
            bot.delete_message(message.chat.id, message.message_id)
            
            try:
                bot.delete_message(prev_id, prev_message)
            except:
                a = 1
        
            markup_1 = types.InlineKeyboardMarkup(row_width = 2)
            item1 = types.InlineKeyboardButton('Фильм', callback_data = 'watch_film')
            item2 = types.InlineKeyboardButton('Сериал', callback_data = 'watch_series')
            markup_1.add(item1, item2)
            prev_message = bot.send_message(message.chat.id, "Что вы хотите посмотреть?", reply_markup = markup_1) 
            prev_id = prev_message.chat.id
            prev_message = prev_message.message_id
            
        elif message.text == 'Скачать mp4':
            bot.delete_message(message.chat.id, message.message_id)
            
            try:
                bot.delete_message(prev_id, prev_message)
            except:
                a = 1
                
            markup_1 = types.InlineKeyboardMarkup(row_width = 2)
            item1 = types.InlineKeyboardButton('Фильм', callback_data = 'download_film')
            item2 = types.InlineKeyboardButton('Сериал', callback_data = 'download_series')
            markup_1.add(item1, item2)
            prev_message = bot.send_message(message.chat.id, "Что вы хотите скачать?", reply_markup = markup_1)  
            prev_id = prev_message.chat.id
            prev_message = prev_message.message_id                   
        
            
             
# выбор для просмотра фильмов онлайн
def user_choise_film_online(message):
    global prev_message
    global prev_id
    
    if message.text == 'Смотреть онлайн':
        movie_start(message)
        
    elif message.text == 'Скачать mp4':
        movie_start(message)
        
    elif message.text != 'Смотреть онлайн' and message.text != 'Скачать mp4':
        sticker = bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIad2KaG5EosEgBkEAM78EScDyreuonAAJBAQACzRswCPHwYhjf9pZYJAQ')
        list_pages = get_list_movie_online(message.text)
        
        for movie in list_pages:
            list_movie[movie] = list_pages[movie]
        
        markup_inline = types.InlineKeyboardMarkup(row_width = 1)
        cnt = 1
        
        for movie in list_movie:
            sign = str(cnt) + '_wf'
            item = types.InlineKeyboardButton(movie, callback_data = sign)
            list_number[str(cnt)] = movie
            markup_inline.add(item)
            cnt += 1
            
            if cnt == 11:
                break
            
        bot.delete_message(message.chat.id, sticker.message_id)
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(prev_id, prev_message)
        
        if cnt == 1:
            request_movie = bot.send_message(message.chat.id, "Извините, не смог ничего найти\n"
                                            "Попробуйте ввести название фильма еще раз")
            
            prev_message = request_movie.message_id
            prev_id = request_movie.chat.id
            bot.register_next_step_handler(request_movie, user_choise_film_online)
                
        else:
            item_other = types.InlineKeyboardButton('В списке нет нужного фильма', callback_data = 'accurately_film_online')
            markup_inline.add(item_other)
            prev_message = bot.send_message(message.chat.id, "Вот что мне удалось найти по вашему запросу:", reply_markup = markup_inline)
            prev_id = prev_message.chat.id
            prev_message = prev_message.message_id 
        


# выбор для просмотра сериалов онлайн
def user_choise_series_online(message):
    global prev_message
    global prev_id
    
    if message.text == 'Смотреть онлайн':
        movie_start(message)
        
    elif message.text == 'Скачать mp4':
        movie_start(message)
        
    elif message.text != 'Смотреть онлайн' and message.text != 'Скачать mp4':
        sticker = bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIad2KaG5EosEgBkEAM78EScDyreuonAAJBAQACzRswCPHwYhjf9pZYJAQ')
        list_pages = get_list_movie_online(message.text)
        
        
        for movie in list_pages:
            list_movie[movie] = list_pages[movie]
        
        markup_inline = types.InlineKeyboardMarkup(row_width = 1)
        cnt = 1
        
        for movie in list_movie:
            sign = str(cnt) + '_ws'
            item = types.InlineKeyboardButton(movie, callback_data = sign)
            list_number[str(cnt)] = movie
            markup_inline.add(item)
            cnt += 1
            
            if cnt == 11:
                break
            
        bot.delete_message(message.chat.id, sticker.message_id)
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(prev_id, prev_message)

        if cnt == 1:
            request_movie = bot.send_message(message.chat.id, "Извините, не смог ничего найти\n"
                                            "Попробуйте ввести название сериала еще раз")
            prev_message = request_movie.message_id
            prev_id = request_movie.chat.id
            bot.register_next_step_handler(request_movie, user_choise_series_online)
            
        else:
            item_other = types.InlineKeyboardButton('В списке нет нужного сериала', callback_data = 'accurately_series_online')
            markup_inline.add(item_other)
            prev_message = bot.send_message(message.chat.id, "Вот что мне удалось найти по вашему запросу:", reply_markup = markup_inline)
            prev_id = prev_message.chat.id
            prev_message = prev_message.message_id
            
        

# выбор для скачивания фильма
def user_choise_film_download(message):
    global prev_message
    global prev_id
    global remember_name
    
    if message.text == 'Смотреть онлайн':
        movie_start(message)
        
    elif message.text == 'Скачать mp4':
        movie_start(message)
        
    elif message.text != 'Смотреть онлайн' and message.text != 'Скачать mp4':
        sticker = bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIad2KaG5EosEgBkEAM78EScDyreuonAAJBAQACzRswCPHwYhjf9pZYJAQ')
        remember_name = message.text
        list_pages = get_list_film_download(message.text)
        
        for movie in list_pages:
            list_movie[movie] = list_pages[movie]
        
        markup_inline = types.InlineKeyboardMarkup(row_width = 1)
        cnt = 1
        
        for movie in list_movie:
            callbackd = str(cnt) + '_df'
            item = types.InlineKeyboardButton(movie, callback_data = callbackd)
            list_number[str(cnt)] = movie
            markup_inline.add(item)
            cnt += 1
            
            if cnt == 11:
                break
            
        bot.delete_message(message.chat.id, sticker.message_id)
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(prev_id, prev_message)

        if cnt == 1:
            request_movie = bot.send_message(message.chat.id, "Извините, не смог ничего найти\n"
                                            "Попробуйте ввести название фильма еще раз")
            prev_message = request_movie.message_id
            prev_id = request_movie.chat.id
            bot.register_next_step_handler(request_movie, user_choise_film_download)
                
        else:
            item_other = types.InlineKeyboardButton('В списке нет нужного фильма', callback_data = 'accurately_film_download')
            markup_inline.add(item_other)
            prev_message = bot.send_message(message.chat.id, "Вот что мне удалось найти по вашему запросу:", reply_markup = markup_inline)
            prev_id = prev_message.chat.id
            prev_message = prev_message.message_id
        
        

# выбор для скачивания сериала
def user_choise_series_download(message):
    global prev_message
    global prev_id
    global remember_name
    
    if message.text == 'Смотреть онлайн':
        movie_start(message)
        
    elif message.text == 'Скачать mp4':
        movie_start(message)
        
    elif message.text != 'Смотреть онлайн' and message.text != 'Скачать mp4':
        sticker = bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIad2KaG5EosEgBkEAM78EScDyreuonAAJBAQACzRswCPHwYhjf9pZYJAQ')
        remember_name = message.text
        list_pages = get_list_series_download(message.text)
        
        for movie in list_pages:
            list_movie[movie] = list_pages[movie]
        
        markup_inline = types.InlineKeyboardMarkup(row_width = 1)
        cnt = 1
        
        for movie in list_movie:
            callbackd = str(cnt) + '_ds'
            item = types.InlineKeyboardButton(movie, callback_data = callbackd)
            list_number[str(cnt)] = movie
            markup_inline.add(item)
            cnt += 1
            
            if cnt == 11:
                break
            
        bot.delete_message(message.chat.id, sticker.message_id)
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(prev_id, prev_message)

        if cnt == 1:
            request_movie = bot.send_message(message.chat.id, "Извините, не смог ничего найти\n"
                                            "Попробуйте ввести название сериала еще раз")
            prev_message = request_movie.message_id
            prev_id = request_movie.chat.id
            bot.register_next_step_handler(request_movie, user_choise_series_download)
                
        else:
            item_other = types.InlineKeyboardButton('В списке нет нужного сериала', callback_data = 'accurately_series_download')
            markup_inline.add(item_other)
            prev_message = bot.send_message(message.chat.id, "Вот что мне удалось найти по вашему запросу:", reply_markup = markup_inline)
            prev_id = prev_message.chat.id
            prev_message = prev_message.message_id
        


@bot.callback_query_handler(func = lambda call: True)
def callback_inline(call):
    if call.message:
        global prev_message
        global prev_id
        global request_movie
        global remember_name
        global wrong_movie
        global wrong_id
        global image_msg
        global text_msg
        global cnt_ser
        
        if call.data == 'watch_film':
            list_movie.clear()
            list_number.clear()
            request_movie = bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'Введите название фильма, который хотите посмотреть', reply_markup = None)
            prev_message = request_movie.message_id
            prev_id = request_movie.chat.id
            bot.register_next_step_handler(request_movie, user_choise_film_online)
            
        if call.data[-2:] == 'wf':
            s = call.data
            my_string = s.split("_")
            ind = my_string[0]
            bot.delete_message(call.message.chat.id, call.message.message_id)
            sticker = bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAIad2KaG5EosEgBkEAM78EScDyreuonAAJBAQACzRswCPHwYhjf9pZYJAQ')
            page = list_movie[list_number[ind]]
            
            about_movie = get_movie_online(page)
            url_image = about_movie[0]
            url_movie = about_movie[1]
            
            spl_string = list_number[ind].split()
            rm = spl_string[:-1]
            name = ' '.join([str(elem) for elem in rm])
            name = '🎥 ' + name
            info_movie = name + '\n\n' + about_movie[2]
            
            markup_watch_online = types.InlineKeyboardMarkup(row_width = 1)
            item1 = types.InlineKeyboardButton("Перейти к просмотру", url = url_movie)
            markup_watch_online.add(item1)
            bot.delete_message(call.message.chat.id, sticker.message_id)
            
            try:
                box = bot.send_photo(call.message.chat.id, url_image, info_movie, reply_markup = markup_watch_online)
            except:
                box = bot.send_message(call.message.chat.id, info_movie, reply_markup = markup_watch_online)
                
            bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAIahmKby6PHsfTIOUtfyxKp0nf7MqnrAAINAANIRaMek6LDXEnJb_UkBA')
            wrong_movie = box.message_id
            wrong_id = box.chat.id
            
        if call.data == 'accurately_film_online':
            request_movie = bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'Введите более точное название фильма', reply_markup = None)
            list_movie.clear()
            list_number.clear()
            prev_message = request_movie.message_id
            prev_id = request_movie.chat.id
            bot.register_next_step_handler(request_movie, user_choise_film_online)
            
        if call.data == 'another_watch_film':
            bot.delete_message(wrong_id, wrong_movie)
            request_movie = bot.send_message(call.message.chat.id, 'Введите название фильма еще раз')
            list_movie.clear()
            list_number.clear()
            prev_message = request_movie.message_id
            prev_id = request_movie.chat.id
            bot.register_next_step_handler(request_movie, user_choise_film_online)
            
            
            
    
        if call.data == 'watch_series':
            list_movie.clear()
            list_number.clear()
            request_movie = bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'Введите название сериала, который хотите посмотреть', reply_markup = None)
            prev_message = request_movie.message_id
            prev_id = request_movie.chat.id
            bot.register_next_step_handler(request_movie, user_choise_series_online)

        if call.data[-2:] == 'ws':
            s = call.data
            my_string = s.split("_")
            ind = my_string[0]
            bot.delete_message(call.message.chat.id, call.message.message_id)
            sticker = bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAIad2KaG5EosEgBkEAM78EScDyreuonAAJBAQACzRswCPHwYhjf9pZYJAQ')
            page = list_movie[list_number[ind]]
            
            about_movie = get_movie_online(page)
            
            url_image = about_movie[0]
            url_movie = about_movie[1]
            
            spl_string = list_number[ind].split()
            rm = spl_string[:-1]
            name = ' '.join([str(elem) for elem in rm])
            name = '🎥 ' + name
            info_movie = name + '\n\n' + about_movie[2]
            
            markup_watch_online = types.InlineKeyboardMarkup(row_width = 1)
            item1 = types.InlineKeyboardButton("Перейти к просмотру", url = url_movie)
            markup_watch_online.add(item1)
            bot.delete_message(call.message.chat.id, sticker.message_id)
            box = bot.send_photo(call.message.chat.id, url_image, info_movie, reply_markup = markup_watch_online)
            bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAIahmKby6PHsfTIOUtfyxKp0nf7MqnrAAINAANIRaMek6LDXEnJb_UkBA')
            wrong_movie = box.message_id
            wrong_id = box.chat.id
            
        if call.data == 'accurately_series_online':
            request_movie = bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'Введите более точное название сериала', reply_markup = None)
            list_movie.clear()
            list_number.clear()
            prev_message = request_movie.message_id
            prev_id = request_movie.chat.id
            bot.register_next_step_handler(request_movie, user_choise_series_online)
            
        if call.data == 'another_watch_series':
            bot.delete_message(wrong_id, wrong_movie)
            request_movie = bot.send_message(call.message.chat.id, 'Введите название сериала еще раз')
            list_movie.clear()
            list_number.clear()
            prev_message = request_movie.message_id
            prev_id = request_movie.chat.id
            bot.register_next_step_handler(request_movie, user_choise_series_online)
            
            
        
            
        if call.data == 'download_film':
            list_movie.clear()
            list_number.clear()
            request_movie = bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'Введите название фильма, который хотите скачать', reply_markup = None)
            prev_message = request_movie.message_id
            prev_id = request_movie.chat.id
            bot.register_next_step_handler(request_movie, user_choise_film_download)
            
        if call.data[-2:] == 'df':
            s = call.data
            my_string = s.split("_")
            ind = my_string[0]
            bot.delete_message(call.message.chat.id, call.message.message_id)
            sticker = bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAIad2KaG5EosEgBkEAM78EScDyreuonAAJBAQACzRswCPHwYhjf9pZYJAQ')
            
            spl_string = list_number[ind].split()
            rm = spl_string[:-1]
            global full_name
            full_name = ' '.join([str(elem) for elem in rm])
            about_movie = get_film_download(remember_name, full_name)
            
            url_image = about_movie[0]
            url_movie = about_movie[1]
            
            name = '🎥 ' + full_name
            info_movie = name + '\n\n' + about_movie[2]
            
            markup_download = types.InlineKeyboardMarkup(row_width = 1)
            item1 = types.InlineKeyboardButton("Скачать", url = url_movie)
            markup_download.add(item1)
            bot.delete_message(call.message.chat.id, sticker.message_id)
            box = bot.send_photo(call.message.chat.id, url_image, info_movie, reply_markup = markup_download)
            bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAIahmKby6PHsfTIOUtfyxKp0nf7MqnrAAINAANIRaMek6LDXEnJb_UkBA')
            wrong_movie = box.message_id
            wrong_id = box.chat.id
            
        if call.data == 'accurately_film_download':
            request_movie = bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'Введите более точное название фильма', reply_markup = None)
            list_movie.clear()
            list_number.clear()
            prev_message = request_movie.message_id
            prev_id = request_movie.chat.id
            bot.register_next_step_handler(request_movie, user_choise_film_download)
            
        if call.data == 'another_download_film':
            bot.delete_message(wrong_id, wrong_movie)
            request_movie = bot.send_message(call.message.chat.id, 'Введите название фильма еще раз')
            list_movie.clear()
            list_number.clear()
            prev_message = request_movie.message_id
            prev_id = request_movie.chat.id
            bot.register_next_step_handler(request_movie, user_choise_film_download)
            
            
        
        
        if call.data == 'download_series':
            list_movie.clear()
            list_number.clear()
            request_movie = bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'Введите название сериала, который хотите скачать', reply_markup = None)
            prev_message = request_movie.message_id
            prev_id = request_movie.chat.id
            bot.register_next_step_handler(request_movie, user_choise_series_download)
            
        if call.data[-2:] == 'ds':
            s = call.data
            my_string = s.split("_")
            ind = my_string[0]
            bot.delete_message(call.message.chat.id, call.message.message_id)
            sticker = bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAIad2KaG5EosEgBkEAM78EScDyreuonAAJBAQACzRswCPHwYhjf9pZYJAQ')
            
            spl_string = list_number[ind].split()
            rm = spl_string[:-1]
            full_name = ' '.join([str(elem) for elem in rm])
            about_movie = get_series_download(remember_name, full_name)
            url_image = about_movie[0]
            list_series = about_movie[1]
            name = '🎥 ' + full_name
            info_movie = name + '\n\n' + about_movie[2]

            markup_download_series = types.InlineKeyboardMarkup(row_width = 2)
            cnt = 1
            
            for ser in list_series:
                back = str(cnt) + '_dn'
                item =  types.InlineKeyboardButton(ser, callback_data = back)
                markup_download_series.add(item)
                cnt += 1
                
            cnt_ser = cnt
                
            item =  types.InlineKeyboardButton('Все сезоны', callback_data = 'all_ser')
            markup_download_series.add(item)
            
            bot.delete_message(call.message.chat.id, sticker.message_id)
            box = bot.send_photo(call.message.chat.id, url_image, info_movie, reply_markup = markup_download_series)
            prev_message = box.message_id
            prev_id = box.chat.id
            image_msg = url_image
            text_msg = info_movie
        
        if call.data[-2:] == 'dn':
            bot.delete_message(prev_id, prev_message)
            bot.send_photo(call.message.chat.id, image_msg, text_msg)
            bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAIahmKby6PHsfTIOUtfyxKp0nf7MqnrAAINAANIRaMek6LDXEnJb_UkBA')
            s = call.data
            my_string = s.split("_")
            ind = my_string[0]
            
            sticker = bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAIad2KaG5EosEgBkEAM78EScDyreuonAAJBAQACzRswCPHwYhjf9pZYJAQ')
            
            list_of_ser = get_list_of_ser_download(remember_name, full_name, int(ind))
            markup_3 = types.InlineKeyboardMarkup(row_width = 1)
            
            for ser in list_of_ser:
                item = types.InlineKeyboardButton(ser, url = list_of_ser[ser])
                markup_3.add(item)
                
            ind = '🎬 Сезон ' + ind
            bot.delete_message(call.message.chat.id,sticker.message_id)
            bot.send_message(call.message.chat.id, '🎥 ' + full_name + '\n' + ind, reply_markup = markup_3)
            bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAIahmKby6PHsfTIOUtfyxKp0nf7MqnrAAINAANIRaMek6LDXEnJb_UkBA')
            
            
            
            
        if call.data == 'all_ser':
            bot.delete_message(prev_id, prev_message)
            bot.send_photo(call.message.chat.id, image_msg, text_msg)
            bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAIahmKby6PHsfTIOUtfyxKp0nf7MqnrAAINAANIRaMek6LDXEnJb_UkBA')
            
            for i in range(1, cnt_ser):
                sticker = bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAIad2KaG5EosEgBkEAM78EScDyreuonAAJBAQACzRswCPHwYhjf9pZYJAQ')
                list_of_ser = get_list_of_ser_download(remember_name, full_name, i)
                markup_3 = types.InlineKeyboardMarkup(row_width = 1)
                
                for ser in list_of_ser:
                    item = types.InlineKeyboardButton(ser, url = list_of_ser[ser])
                    markup_3.add(item)
    
                bot.delete_message(call.message.chat.id, sticker.message_id)
                bot.send_message(call.message.chat.id, '🎥 ' + full_name + '\n' + '🎬 Сезон ' + str(i), reply_markup = markup_3)
                bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAIahmKby6PHsfTIOUtfyxKp0nf7MqnrAAINAANIRaMek6LDXEnJb_UkBA')
            
            
        if call.data == 'accurately_series_download':
            request_movie = bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'Введите более точное название сериала', reply_markup = None)
            list_movie.clear()
            list_number.clear()
            prev_message = request_movie.message_id
            prev_id = request_movie.chat.id
            bot.register_next_step_handler(request_movie, user_choise_series_download)

        if call.data == 'another_download_series':
            bot.delete_message(wrong_id, wrong_movie)
            request_movie = bot.send_message(call.message.chat.id, 'Введите название сериала еще раз')
            list_movie.clear()
            list_number.clear()
            prev_message = request_movie.message_id
            prev_id = request_movie.chat.id
            bot.register_next_step_handler(request_movie, user_choise_series_download)
            
            
# bot.infinity_polling(timeout=10, long_polling_timeout = 5) - на удаденном серевере linux
bot.polling(none_stop = True)   # на локальном компьютере