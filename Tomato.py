class Tomato:
    # Стадии созревания помидора
    states = {0: 'ничего нет', 1: 'появился цветок', 2: 'есть зелёный помидор', 3: 'помидор созрел'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):

        if self._state < 3:
            self._state += 1
        print(f'Помирод {self._index} состояние: {Tomato.states[self._state]}')

    def is_ripe(self):
        if self._state == 3:
            return True
        return False