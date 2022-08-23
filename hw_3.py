while(True):
    str = input('Введите число или "exit" для остановки: ')
    if str.lower() == 'exit':
        break
    else:
        try:
            num = float(str)
            print('Correct')
        except:
            print('Wrong')