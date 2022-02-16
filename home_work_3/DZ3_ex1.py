def num_tanslate(number):
    translator = {'zero': 'ноль',
            'one': 'один',
            'two': 'два',
            'three': 'три',
            'four': 'четыре',
            'five': 'пять',
            'six': 'шесть',
            'seven': 'семь',
            'eight': 'восемь',
            'nine': 'девять',
            'ten': 'десять'}
    return translator.get(number)


print(num_tanslate('eight'))
