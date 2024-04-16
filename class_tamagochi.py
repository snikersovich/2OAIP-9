class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50
        self.is_alive = True

    def feed(self):
        if self.is_alive:
            print(f'{self.name} поел и сыт')
            self.hunger += 10
            self.energy -= 5
            self.happiness += 5
        else:
            print(f'{self.name} уже умер')

    def sleep(self):
        if self.is_alive:
            print(f'{self.name} поспал и отдохнул')
            self.energy += 15
            self.hunger -= 5
            self.happiness += 5
        else:
            print(f'{self.name} уже умер')

    def play(self):
        if self.is_alive:
            print(f'{self.name} поиграл и счастлив')
            self.hunger -= 5
            self.energy -= 5
            self.happiness += 10
        else:
            print(f'{self.name} уже умер')

    def check_status(self):
        if self.hunger <= 0 or self.energy <= 0 or self.happiness <= 0:
            self.is_alive = False
            print(f'{self.name} умер от голода, усталости или грусти. Капец ему кароче')
        else:
            print(f'{self.name}: Голод - {self.hunger}, Энергия - {self.energy}, Счастье - {self.happiness}')


pet1 = Pet('Тузик')

pet1.check_status()
pet1.feed()
pet1.sleep()
pet1.play()
pet1.check_status()