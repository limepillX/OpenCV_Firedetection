from datetime import datetime

def main_print(color_code, text):
    time_now = str(datetime.now().time())[:8]
    print(f'[{time_now}]\t \x1b[{color_code}m ' + str(text) + ' \x1b[0m \n')
    

def custom(color, s):
    palette = {
        'green': '6;30;42',
        'red': '0;30;41',
        'white': '0;30;47',
        'blue': '0;37;44'
    }
    main_print(palette[color], s)

def sucsess(s):
    main_print('0;37;42', s)

def warning(s):
    main_print('0;37;43', s)

def danger(s):
    main_print('0;30;41', s)

def text(s):
    main_print('0;30;47', s)