# Тесты
from Gardener import Gardener
from TomatoBush import TomatoBush

if __name__ == '__main__':
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Иван', great_tomato_bush)
    gardener.knowledge_base()

    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()
