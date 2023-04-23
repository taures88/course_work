import json

"""загружаем файл json"""


def load_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


"""фильтруем список json и выводим последние 5 выполненных EXECUTED и сортируем по дате убывания"""


def sort_file(data):
    new_data = []
    for item in data:
        if item.get('state') == 'EXECUTED':
            new_data.append(item)
    new_data = sorted(new_data, key=lambda item: item['date'], reverse=True)
    return new_data


"""Выводим операции карт и счетов"""


def form_data(item):
    item_date = format_date(item.get("date"))

    """перевод с карты на карту, с карты на счет или со счета на счет"""
    if item.get("from"):
        from_ = mask_card(item.get("from")) + ' -> '
    else:
        """открытие вклада"""
        from_ = ''
    to_ = mask_card(item.get("to"))
    return f'{item_date} {item.get("description")}\n' \
           f'{from_}{to_}\n' \
           f'{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}\n'


"""Выводим правильно дату отобразив её обратно начиная дата.месяц.год"""


def format_date(srt_date):
    list_date = srt_date[:10].split('-')
    return '.'.join(reversed(list_date))


"""Выводим замаскированный формат карты или счета"""


def mask_card(card):
    card = card.split(' ')
    if card[0] == 'Счет':
        return f'{card[0]} **{card[-1][-4:]}'
    return f'{" ".join(card[:-1])} {card[-1][:4]} {card[-1][4:6]}** **** {card[-1][-4:]}'



