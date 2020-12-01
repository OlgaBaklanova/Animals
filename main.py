class Bird:
    def __init__(self, title_animal, nickname, voice, weight, eat, bonuses):
        self.title_animal = title_animal
        self.nickname = nickname
        self.voice = voice
        self.weight = weight
        self.eat = eat
        self.bonuses = bonuses

    def eating(self, kg):
        return self.eat * kg

    def collecting_eggs(self, quantity):
        return quantity


grey = Bird('Гусь', 'Серый', 'Кря', 5, 2, 'Яйца')
white = Bird('Гусь', 'Белый', 'Кря', 7, 2, 'Яйца')
coco = Bird('Курица', 'Ко-ко', 'Кудах', 3, 2, 'Яйца')
cucareca = Bird('Курица', 'Кукареку', 'Кудах', 4, 2, 'Яйца')
cryakva = Bird('Утка', 'Кряква', 'Кря', 5, 2, 'Яйца')


class Ungulates:
    def __init__(self, title_animal, nickname, voice, weight, eat, bonuses):
        self.title_animal = title_animal
        self.nickname = nickname
        self.voice = voice
        self.weight = weight
        self.eat = eat
        self.bonuses = bonuses

    def eating(self, kg):
        return self.eat * kg

    def collecting_milk(self, liter):
        return liter

    def collecting_wool(self, kg):
        return kg


manka = Ungulates('Корова', 'Манька', 'Му', 80, 3, 'Молоко')
barashek = Ungulates('Овца', 'Барашек', 'Бе', 50, 3, 'Шерсть')
kudryavy = Ungulates('Овца', 'Кудрявый', 'Бе', 55, 3, 'Шерсть')
roga = Ungulates('Коза', 'Рога', 'Ме', 30, 3, 'Молоко')
kopyta = Ungulates('Коза', 'Копыта', 'Ме', 40, 3, 'Молоко')

dict_a = {grey.nickname: grey.weight, white.nickname: white.weight, coco.nickname: coco.weight,
          cucareca.nickname: cucareca.weight, cryakva.nickname: cryakva.weight, manka.nickname: manka.weight,
          barashek.nickname: barashek.weight, kudryavy.nickname: kudryavy.weight, roga.nickname: roga.weight,
          kopyta.nickname: kopyta.weight}

count = 0
for weight_a in dict_a.values():
    count += weight_a
print(f'Общий вес животных: {count}')

max_count = 0
animal_max = 0
for i, y in dict_a.items():
    if max_count < y:
        max_count = y
        animal_max = i

print(f'Самое тяжелое животное: {animal_max}')
print(f'Молока сегодня {manka.collecting_milk(3)} литра')
print(f'Кряква съела {cryakva.eating(0.5)} кг зерна')
print(f'Ко-ко снесла {coco.collecting_eggs(2)}')