from function import load_json, sort_file, form_data

j_file = 'operations.json'

"""основная функция которая запускает программу, загружает файлы и выводит 5 операций"""


def main():
    data = load_json(j_file)
    data = sort_file(data)

    for i in range(5):
        print(form_data(data[i]))


if __name__ == '__main__':
    main()
