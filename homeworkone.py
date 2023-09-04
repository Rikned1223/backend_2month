class SuperHero:
    people = 'people'
    def __init__(self, name, nickname, superpower,health_points,catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def hero_name(self):
        print(f'Имя героя:{self.name}')

    def double_health(self):
        return f'Здоровье: {self.health_points * 2}'

    def __str__(self):
        return f'Прозвище героя: {self.nickname},' \
               f'Суперспособность: {self.superpower}, ' \
               f'Здоровье героя: {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero('Rustam', 'Albaruss', 'Bomb', 100, 'Бам бам бам')
hero.hero_name()
hero.double_health()
print(hero)
print(len(hero))

class Avatar(SuperHero):
    people = 'people'
    def __init__(self,name, nickname, superpower,health_points,catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def double_health(self):
        self.fly = True
        print(f'Здоровье: {self.health_points ** 2}')

    def phrase(self):
        print(f'Fly in the {self.fly}_phrase')

avatar = Avatar('Avatar', 'Ava', 'heal', 500, 'Слава роду,слава русскому народу', 200, 'Крылья')
avatar.double_health()
avatar.phrase()
print(avatar)

class Naruto(SuperHero):
    people = 'people'
    def __init__(self,name, nickname, superpower,health_points,catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def double_health(self):
        self.fly = True
        print(f'Здоровье: {self.health_points ** 2}')

    def phrase(self):
        print(f'Fly in the {self.fly}_phrase')

naruto = Naruto('Naruto', 'Hokage', 'Water', 1000, 'Я стану хокаге даттебае', 400, '9 хвостый')
naruto.double_health()
naruto.phrase()
print(naruto)

class Villain(Avatar):
    def __init__(self,name, nickname, superpower,health_points,catchphrase):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        Avatar.people = 'monster'

    def gen_x(self):
        pass

    def crit(self,hero):
        return hero.damage ** 2
        print(damage)

vaillain = Villain('Villain', 'Vilya', 'Fire', 5000, 'Мир падет к ногам нашей власти!')
print(Villain.crit(vaillain, naruto))





