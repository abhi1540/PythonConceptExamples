
class Employee(object):

    def __init__(self, emp_id, first_name, last_name, salary, age):
        self._emp_id = emp_id
        self._first_name = first_name
        self._last_name = last_name
        self._salary = salary
        self._age = age

    @property
    def emp_id(self):
        return self._emp_id

    @emp_id.setter
    def emp_id(self, emp_id):
        self._emp_id = emp_id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age > 18:
            self._age = age
        else:
            raise ValueError("Enter age greater than 18")

    def __str__(self):
        return '{}-{}-{}-{}-{}'.format(self._emp_id, self._first_name, self._last_name, self._salary, self._age)


obj = Employee(1, 'abhisek', 'gantait', 10000, 28)
obj.__age = 30

print(obj) ## it will print 28 because you can't set the value outside
# output: 1-abhisek-gantait-10000-28


# MyClass.__private just becomes MyClass._MyClass__private


class A(object):
    def __method(self):
        print("I'm a method in A")

    def method(self):
        self.__method()


class B(A):
    def __method(self):
        print("I'm a method in B")


a = A()
a.method() #I'm a method in A
b = B()
b.method() #I'm a method in A


# def our_decorator(func):
#     def function_wrapper(x):
#         print("Before calling " + func.__name__)
#         func(x)
#         print("After calling " + func.__name__)
#
#     return function_wrapper
#
#
# def foo(x):
#     print("Hi, foo has been called with " + str(x))
#
#
# print("We call foo before decoration:")
# foo("Hi")
#
# print("We now decorate foo with f:")
# foo = our_decorator(foo)
#
# print("We call foo after decoration:")
# foo(42)


def log_instance(my_log):
    def outerwrapper(cls_):
        def wrapper_method(self):
            my_log.info(
                'Instance of {name} @ {id:X}: {dict}'.format(name=cls_.__name__, id=id(self), dict=repr(self.__dict__)))

        cls_.log_instance = wrapper_method
        cls_.log_instance.__name__ = 'log_instance'
        cls_.log_instance.__doc__ = 'Generate log message with the details of this instance'

        return cls_

    return outerwrapper


import logging
mylog = logging.getLogger('my_logger')
mylog.setLevel(logging.INFO)

@log_instance(mylog)
class Hello(object):

 def __init__(self, str):
   self.str = str
 def speak(self):
   
   print('Hello {}'.format(self.str))

inst = Hello('Tony')
inst.speak()