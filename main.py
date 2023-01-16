class Tomato:
    # Стадии созревания помидора
    states = {1: 'ничего нет', 2: 'появился цветок', 3: 'есть зелёный помидор', 4: 'помидор созрел'}

    def __init__(self, index):
        self._index = index
        self._state = 1

    # Переход к следующей стадии созревания
    def grow(self):
        self._change_state()

    # Проверка, созрел ли томат
    def is_ripe(self):
        if self._state == 4:
            return True
        return False

    # Защищенные(protected) методы

    def _change_state(self):
        if self._state < 4:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Помирод {self._index} состояние: {Tomato.states[self._state]}')

class TomatoBush:

    # Создаем список из объектов класса Tomato
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(1, num)]

    # Переводим все томаты из списка на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяем, все ли помидоры созрели
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    # Собираем урожай
    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    # Выдаем садовнику растение для ухода
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # Ухаживаем за растением
    def work(self):
        print(f'Садовник {self.name} работает...')
        self._plant.grow_all()
        print(f'Садовник {self.name} закончил свою работу по уходу за растением')

    # Собираем урожай
    def harvest(self):
        print(f'Садовник {self.name} собирает урожай...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Сбор урожая закончен')
        else:
            print('Слишком рано! Ваши помидорки ещё зелёные!')

    # Статический метод
    # Выводит справку по садоводству
    @staticmethod
    def knowledge_base():
        print('''
        Существует тонкая грань при сборе томатов на стадии зрелой зелени. 
        Обратите внимание на первый легкий румянец цвета как индикатор того, когда собирать помидоры, чтобы не потерять их сущность. 
        Конечно, вы также можете собирать плоды томатов, когда они созреют; спелые плоды утонут в воде. 
        Эти помидоры, созревшие на виноградной лозе, могут быть 
        самыми сладкими, но некоторые виды томатов слишком тяжелые для созревания на лозе, поэтому помидоры собирают на стадии зрелой
        зелени и позволяют газообразному этилену продолжать процесс созревания.''')


# Тесты
if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(5)
    gardener = Gardener('Иван', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()
