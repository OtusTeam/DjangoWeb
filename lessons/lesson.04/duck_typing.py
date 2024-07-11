# Утиная типизация

# Полиморфизм - утиная типизация


class Car:

    def show(self):
        print('I am car')


class Hamburger:

    def show(self):
        pass


def duck_typing(obj):
    obj.show()


car = Car()
hamburger = Hamburger()

duck_typing(car)
duck_typing(hamburger)

print(
    len([1, 2, 3])
)

print(
    len('some str')
)


print(duck_typing(car))
print(duck_typing)

print(car)


print(dir(car))
print('*'*100)
print(dir(duck_typing))
