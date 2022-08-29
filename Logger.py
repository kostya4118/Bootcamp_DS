import datetime, os

class Logger():
    last = None
    def __init__(self, path='./'):
        self.event = None
        self.path = path

    def __new__(cls, *args):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Logger, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def __get_date():
        now = datetime.datetime.now()
        today = now.strftime("%d:%m:%y")
        time_ = now.strftime("%H:%M:%S")
        return today, time_

    def write_log(self, event):
        try:
            with open(f'{self.path}log_{self.__get_date()[0]}', 'a', encoding='utf-8') as f:
                s = f'[{self.__get_date()[1]}] - {event}\n'
                f.write(s)
                self.last = s
        except FileNotFoundError:
            print('Указанная папка не найдена. create_dir() для создания.')

    def create_dir(self):
        try:
            os.mkdir(self.path)
        except FileExistsError:
            print("Папка уже создана")

    def clear_log(self):
        try:
            with open(f'{self.path}log_{self.__get_date()[0]}', 'w', encoding='utf-8') as f:
                f.write('')
        except FileNotFoundError:
            print('Указанная папка не найдена. create_dir() для создания.')

    def get_logs(self):
        try:
            with open(f'{self.path}log_{self.__get_date()[0]}', 'r', encoding='utf-8') as f:
                text = f.readlines()
                result = []
                for el in text:
                    result.append(tuple(el[1:-1].split('] - ')))
            return result
        except FileNotFoundError:
            return  f'На сегодня логов нет либо указанная папка не найдена. create_dir() для создания.'

    def get_last_event(self):
        try:
            if self.last:
                return self.last
            file = self.get_all_logs()[-1]
            with open(file, 'r', encoding='utf-8') as f:
                return f.readlines()[-1]
        except AttributeError:
            return f'Событий нет.'
        except IsADirectoryError:
            return f'Указанная папка не найдена. create_dir() для создания.'

    def get_all_logs(self):
        try:
            files = os.listdir(self.path)
            result = []
            for f in files:
                if 'log_' in f:
                    result.append(f)
            return result
        except FileNotFoundError:
            return f'Указанная папка не найдена. create_dir() для создания.'


if __name__ == '__main__':

    logger = Logger('./logs/')
    logger2 = Logger('./logs/')
    print(logger)
    print(logger2)

    # logger.create_dir()
    logger.write_log('событие')
    # logger.clear_log()
    print(logger2.get_last_event())
    print(logger.get_all_logs())
    print(logger.get_logs())