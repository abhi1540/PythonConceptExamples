# Duck Typing and Easier to ask forgiveness than permission (EAFP)


class Duck:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')


class Person:

    def quack(self):
        print("I'm Quacking Like a Duck!")

    def fly(self):
        print("I'm Flapping my Arms!")

# it doesn't matter what object(here thing) u are passing unless it has same methods
def quack_and_fly(thing):

        try:
            thing.quack()
            thing.fly()
            thing.bark()
        except AttributeError as e:
            print(e)

d = Duck()
p = Person()
# we don't worry which object it is, if that object has same methods then it should execute
quack_and_fly(d)
quack_and_fly(p)