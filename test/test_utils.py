from function import load_json, sort_file, form_data, format_date, mask_card


def test_load_json():
    list_test = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    ]
    assert load_json('test.json') == list_test


def test_sort_file():
    list_ = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041"
        },
        {
            "id": 2,
            "state": "OPEN",
            "date": "2016-07-03T18:35:29.512364"
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572"
        }

    ]
    sorted_list = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041"
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572"
        }

    ]

    assert sort_file(list_) == sorted_list


def test_form_data():
    file_1 = {
        "id": 154927927,
        "state": "EXECUTED",
        "date": "2019-11-19T09:22:25.899614",
        "operationAmount": {
            "amount": "30153.72",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 7810846596785568",
        "to": "Счет 43241152692663622869"
    }

    file_2 = '19.11.2019 Перевод организации\n' \
             'Maestro 7810 84** **** 5568 -> Счет **2869\n' \
             '30153.72 руб.\n'
    file_3 = {
        "id": 108066781,
        "state": "EXECUTED",
        "date": "2019-06-21T12:34:06.351022",
        "operationAmount": {
            "amount": "25762.92",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 90817634362091276762"
    }

    file_4 = '21.06.2019 Открытие вклада\n' \
             'Счет **6762\n' \
             '25762.92 руб.\n'

    assert form_data(file_1) == file_2
    assert form_data(file_3) == file_4


def test_format_date():
    assert format_date('2018-04-04T17:33:34.701093') == '04.04.2018'
    assert format_date('2019-09-11T17:30:34.445824') == '11.09.2019'


def test_mask_card():
    assert mask_card("Master Card 4047671689373225") == 'Master Card 4047 67** **** 3225'
    assert mask_card("Maestro 3806652527413662") == 'Maestro 3806 65** **** 3662'
    assert mask_card("Счет 24763316288121894080") == 'Счет **4080'
