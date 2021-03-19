# Survival
#
# 1. In the Forest (Iterable) lives Predators and Herbivores (abstract class of animal and two offspring).
# Each animal is born with the following parameters (by using random):
# - strength (from 25 to 100 points)
# - speed (from 25 to 100 points)
# The force cannot be greater than it was at birth (initialization).
#
# At each step of the game we take 1 animal from the forest (iteration):
# - If it is herbivorous, then it eats (restores its strength by 50%).
# - If it is a predator, it hunts - randomly chooses an animal from the forest and:
#     - pulled himself out, he was unlucky and he was left without a dinner;
#     - pulled out another animal, then tries to catch up;
#     - if he can catch up, he catches up and attacks;
#     - if attacked and is stronger, then eats and restores 50% of strength;
#     - did not catch up or did not have enough strength, then he and the lucky prey lose 30% of strength (Because both either ran, or fought, or all together)
#
# An animal whose power has expired dies. (You can check the strength at the time of food search)
#
# The game continues as long as predators are present in the forest.


from __future__ import annotations
from typing import Dict, Any
from abc import ABC, abstractmethod
import random
import uuid
import time


class Animal(ABC):

    def __init__(self, power: int, speed: int):
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        raise NotImplementedError


class Predator(Animal):
    def __init__(self, power: int, speed: int):
        super().__init__(power, speed)
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    def eat(self, forest: Forest):
        target = random.choice(list(forest.animals.values()))
        if target.id == self.id:
            print('Predator did not find animals in forest')
        else:
            if (self.speed > target.speed) and (self.current_power > target.current_power):
                print('Predator eating...')
                tmp = self.current_power
                self.current_power = min(self.current_power + self.max_power * 0.5, self.max_power)
                print(f'Predator restored {self.current_power - tmp} power')
                forest.animals[target.id].current_power = 0
            else:
                print('Predator did not caught target, both are tired')
                self.current_power = self.current_power - 0.3 * self.max_power
                forest.animals[target.id].current_power = forest.animals[target.id].current_power - 0.3 * \
                                                          forest.animals[target.id].max_power

    def __str__(self):
        return f'{self.__class__.__name__}'


class Herbivorous(Animal):
    def __init__(self, power: int, speed: int):
        super().__init__(power, speed)
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    def __str__(self):
        return f'{self.__class__.__name__}'

    def eat(self, forest: Forest):
        print('Herbivorous eating...')
        tmp = self.current_power
        self.current_power = min(self.current_power + self.max_power * 0.5, self.max_power)
        print(f'Herbivorous restored {self.current_power - tmp} power')


AnyAnimal = [Herbivorous, Predator]


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        print('There is new animal', animal)
        self.animals.update({animal.id: animal})

    def remove_animal(self, animal: AnyAnimal):
        print(animal, 'is removed from forest')
        self.animals.pop(animal.id)

    def any_predator_left(self):
        return not all(isinstance(animal, Herbivorous) for animal in self.animals.values())


def animal_generator():
    while True:
        generated_animal = random.choice((Predator(random.randint(25, 100), random.randint(25, 100)),
                                          Herbivorous(random.randint(25, 100), random.randint(25, 100))))
        generated_animal.id = uuid.uuid4()
        yield generated_animal


if __name__ == "__main__":
    nature = animal_generator()

    forest = Forest()
    for i in range(10):
        animal = next(nature)
        forest.add_animal(animal)

    while True:
        animal_to_remove = []
        for animal in forest.animals.values():
            if animal.current_power < 1:
                animal_to_remove.append(animal.id)
        for animal_id in animal_to_remove:
            forest.remove_animal(forest.animals[animal_id])
        if not forest.any_predator_left():
            print('All predators is dead!')
            break
        for animal in forest.animals.values():
            animal.eat(forest=forest)
        time.sleep(1)
