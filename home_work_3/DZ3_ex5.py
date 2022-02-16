# Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх
# списков (по одному из каждого).
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или
# запрещающий повторы слов в шутках (когда каждое слово можно использовать
# только в одной шутке)? Сможете ли вы сделать аргументы именованными?
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes():
    """Creates jokes from words taken from three lists"""
    noun = random.choice(nouns)
    adverb = random.choice(adverbs)
    adjective = random.choice(adjectives)
    joke = f'{noun} {adverb} {adjective}'
    return joke

print(get_jokes())