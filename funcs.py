def read_file(name_file):
    li = set()
    with open(name_file, 'r', encoding='utf-8') as f:
        for line in f:
            for w in line.split():
                li.add(w.lower())
    return list(li)


def save_file(name_file, list_words):
    with open(name_file, 'w', encoding='utf-8') as f:
        list_words = sorted(list_words)
        for w in list_words:
            f.write(f'{w}\n')
        f.write(f'============================\nВсего в списке {len(list_words)} слов!')


if __name__ is '__main__':
    words = read_file('text.txt')
    save_file('text2.txt', words)

