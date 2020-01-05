# A metaclass is a class that defines properties of other classes.
# With a metaclass, we can define properties that should be added to new classes that are defined in our code.

# hello_metaclass.py
# A simple metaclass
# This metaclass adds a 'hello' method to classes that use the metaclass
# meaning, those classes get a 'hello' method with no extra effort
# the metaclass takes care of the code generation for us
class HelloMeta(type):
    # A hello method
    def hello(cls):
        print("greetings from %s, a HelloMeta type class" % (type(cls())))

    # Call the metaclass
    def __call__(self, *args, **kwargs):
        # create the new class as normal
        cls = type.__call__(self, *args)

        # define a new hello method for each of these classes
        setattr(cls, "hello", self.hello)

        # return the class
        return cls

# Try out the metaclass
class TryHello(object, metaclass=HelloMeta):
    def greet(self):
        self.hello()

# Create an instance of the metaclass. It should automatically have a hello method
# even though one is not defined manually in the class
# in other words, it is added for us by the metaclass
greeter = TryHello()
greeter.greet()



# final.py

# a final metaclass. Subclassing a class that has the Final metaclass should fail
class Final(type):
    def __new__(cls, name, bases, attr):
        # Final cannot be subclassed
        # check that a Final class has not been passed as a base
        # if so, raise error, else, create the new class with Final attributes
        type_arr = [type(x) for x in bases]
        for i in type_arr:
            if i is Final:
                raise RuntimeError("You cannot subclass a Final class")
        return super(Final, cls).__new__(cls, name, bases, attr)


# Test: use the metaclass to create a Cop class that is final

class Cop(metaclass=Final):
    def exit(self):
        print("Exiting...")
        quit()

# Attempt to subclass the Cop class, this should idealy raise an exception!
class FakeCop(Cop):
    def scam(self):
        print("This is a hold up!")

cop1 = Cop()
fakecop1 = FakeCop()

# More tests, another Final class
class Goat(metaclass=Final):
    location = "Goatland"

# Subclassing a final class should fail
class BillyGoat(Goat):
    location = "Billyland"