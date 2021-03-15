from abc import ABC, abstractmethod

VEGETABLES = ['Cherry', 'Red_tomato']
FRUITS = ['Golden', 'King']

states = {'nothing': 0, 'flowering': 1, 'green': 2, 'red': 3, 'rotten': 4}


class GardenMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, *kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Garden(metaclass=GardenMeta):
    def __init__(self, vegetables, fruits, pests, gardener):
        self.vegetables = vegetables
        self.fruits = fruits
        self.pests = pests
        self.gardener = gardener
        self.vegetables_names = [tomato.vegetable_type for tomato in self.vegetables]
        self.fruits_names = [apple.fruits_type for apple in self.fruits]

    def show_the_garden(self):
        print(f'The garden has such vegetables: {self.vegetables_names}')
        print(f'Also garden has such fruits: {self.fruits_names}')
        print(f'And such pests: {self.pests}')
        print(f'The maintainer of the garden is {self.gardener}')


class Vegetables(ABC):
    def __init__(self, states, vegetable_type, name):
        self.states = states
        self.vegetable_type = vegetable_type
        self.name = name

    @property
    def vegetable_type(self):
        return self._vegetable_type

    @vegetable_type.setter
    def vegetable_type(self, vegetable_type):
        if vegetable_type in VEGETABLES:
            self._vegetable_type = vegetable_type
        else:
            raise Exception(f'There is no such vegetable in the list. Your vegetable: {vegetable_type}')

    @abstractmethod
    def grow(self):
        raise NotImplementedError('Your method is not implemented')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError('Your method is not implemented')


class Fruits(ABC):
    def __init__(self, states, fruits_type, name):
        self.states = states
        self.fruits_type = fruits_type
        self.name = name

    @property
    def fruits_type(self):
        return self._fruits_type

    @fruits_type.setter
    def fruits_type(self, fruits_type):
        if fruits_type in FRUITS:
            self._fruits_type = fruits_type
        else:
            raise Exception(f'There is no such fruit in the list. Your fruit: {fruits_type}')

    @abstractmethod
    def grow(self):
        raise NotImplementedError('Your method is not implemented')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError('Your method is not implemented')


class Gardener(ABC):
    def __init__(self, name, plants):
        self.name = name
        self.plants = plants

    @abstractmethod
    def harvest(self):
        raise NotImplementedError('Your method is not implemented')

    @abstractmethod
    def poison_pests(self):
        raise NotImplementedError('Your method is not implemented')

    @abstractmethod
    def handling(self):
        raise NotImplementedError('Your method is not implemented')

    @abstractmethod
    def check_states(self):
        raise NotImplementedError('Your method is not implemented')


class Pests(ABC):
    def __init__(self, pests_type, quantity):
        self.pests_type = pests_type
        self.quantity = quantity

    @abstractmethod
    def eat(self):
        raise NotImplementedError('Your method is not implemented')


class Tomato(Vegetables):
    def __init__(self, index, vegetable_type, states, name):
        super().__init__(states, vegetable_type, name)
        self.index = index
        self.vegetable_type = vegetable_type
        self.state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        else:
            return False

    def _change_state(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print(f'{self.vegetable_type} {self.index} is {self.state}')


class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index, 'Red_tomato', states, 'Cherry') for index in range(0, num - 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def provide_harvest(self):
        self.tomatoes = []

    def __call__(self):
        return self.tomatoes


class Apple(Fruits):
    def __init__(self, index, fruits_type, states, name):
        super(Apple, self).__init__(states, fruits_type, name)
        self.index = index
        self.fruits_type = fruits_type
        self.state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def _change_state(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print(f'{self.fruits_type} {self.index} is {self.state}')


class AppleTrees:
    def __init__(self, num):
        self.apples = [Apple(index, 'Golden', states, 'King') for index in range(0, num - 1)]

    def grow_all(self):
        for apple in self.apples:
            apple.grow()

    def all_are_ripe(self):
        return all([apple.is_ripe() for apple in self.apples])

    def provide_harvest(self):
        self.apples = []

    def __call__(self):
        return self.apples


class StarGardener(Gardener):
    def __init__(self, name, plants):
        super(StarGardener, self).__init__(name, plants)
        self.name = name
        self.plants = plants

    def harvest(self):
        print('Gardener is harvesting...')
        for plant in self.plants:
            if plant.all_are_ripe():
                plant.provide_harvest()
                print('Harvesting is finished.')
            else:
                print('Too early! Your plants is not ripe.')

    def poison_pests(self):
        print('Gardener is searching pests...')
        if Garden().pests.quantity == 0:
            print('There are no pests.')
        else:
            tmp = Garden().pests.quantity
            Garden().pests.quantity = 0
            print(f'{tmp} pests were murdered by gardener.')

    def handling(self):
        print('Gardener is working...')
        for plant in self.plants:
            plant.grow_all()
        print('Gardener is finished.')

    def check_states(self):
        for all_plants in self.plants:
            for plant in all_plants():
                if plant.state == 3:
                    return True
                else:
                    return False

    def __str__(self):
        return f'{self.name}'


class RealPests(Pests):
    def __init__(self, pests_type, quantity):
        super().__init__(pests_type, quantity)

    def eat(self):
        for pest in range(0, self.quantity - 1):
            if len(Garden().vegetables) > 0:
                Garden().vegetables.pop()
                print(f'One Vegetable was eaten, there are {len(Garden().vegetables)} more left.')
            elif len(Garden().fruits) > 0:
                Garden().fruits.pop()
                print(f'One Fruit was eaten, there are {len(Garden().fruits)} more left.')
            else:
                print('There is nothing to eat')

    def __str__(self):
        return f'{self.quantity} {self.pests_type}'


veg_bush = TomatoBush(5)
fruit_tree = AppleTrees(4)
my_pests = RealPests('bug', 10)
peter = StarGardener('Peter', [veg_bush, fruit_tree])
my_garden = Garden(veg_bush.tomatoes, fruit_tree.apples, my_pests, peter)
my_garden.show_the_garden()
# my_garden.pests.eat()
peter.check_states()
for i in range(3):
    peter.handling()
peter.harvest()
