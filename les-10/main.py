class Human:
    def __init__(self, name: str, age: int, is_work: bool):
        self.name = name
        self.age = age
        self.is_work = is_work

    def greetings(self):
        print(f'{self.name} said "Hi"')

    def good_bye(self, name: str):
        print(f'{self.name} said bye to {name}')

    def __str__(self):
        return f'This is man with name {self.name}, age {self.age}'


stone = Human('Kirill', 38, True)
rudolf = Human('Rudolf', 18, True)
# print(stone.age)
# stone.greetings()
# rudolf.greetings()
# stone.good_bye('Rudolf')
# rudolf.good_bye('Kirill')
print(stone)
print(rudolf)
