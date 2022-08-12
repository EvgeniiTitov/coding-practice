### TODO:

- https://refactoring.guru/design-patterns/catalog

---

### General info:

Design patterns are typical solutions to commonly occurring problems in software
design, like pre-made blueprints that could be customized to solve a recurring 
design problem in your code. 

The pattern is not a specific piece of code that could be copied and used, but
a general concept for solving a particular problem.

Often confused with algorithms because both describe typical solutions to some
known problems. Algorithms always define a clear set of actions, while a pattern
is a more high-level description of a solution. The code of the same pattern 
applied to two different programs could be different. 

Design patterns are usually split into 3 categories:

- Creational Patterns
  
  - Deal with the creation (construction) of objects
  - Explicit (constructors) vs implicit (DI, reflection, etc)
  - Wholesale (single statement) vs picewise (step-by-step)

- Structural Patterns

  - Concerned with the structure (assembling objects and classes into larger 
  structures while keeping them flexible and efficient)
  - Many patterns are wrappers that mimic the underlying class's interface
  - Stress the importance of good API design

- Behavioural Patterns

  - Takes cares of effective communication and the assignment of responsibilities
  between objects.

![alt text](../../images/dp.PNG?raw=true)

---

### Summaries:


### Creational patterns

- #### Singleton

The pattern that ensures that a class has only one instance. while providing
a global access point to this instance.

The single responsibility principle solves 2 problems at the same time violating 
the Single Responsibility Princple: 

1. Ensure that a class has just a single instance. 

Why would we want that? the most common reason is to control access to some 
shared resource - a db, a file, etc. Say, we created an object, then we decide 
to create a new one, but instead of getting a fresh one we get the existing one. 

This behaviour is impossible to implement with a regular constructor as it always 
returns a new object


2. Provide a global access point to that instance. 

Just like a global variable, the Singleton pattern lets to access some object
from anywhere in the program while protecting the instance from being overwritten
by other code. 


*Solution*:

All implementations have these 2 common steps:

- Make the default constructor private to prevent other objects from instantiating it directly 
- Create a static creation method / function that acts as a constructor. Under the hood,
it calls the private constructor to create an object and saved it in a static field. 
All following calls to this method return the cached object.

*Pros/Cons*:

| Pros                                                                            | Cons                                                                                                |
|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| A class has only one instance                                                   | Violates the Single Responsibility Principle (solves 2 problems)                                    |
| Global access point to that instance                                            | Requires special treatment in multithreaded code to ensure it doesn't get<br/>created multiple time |
| The singleton object is instantiated only when its requested for the first time |                                                                                                     |
 
*Usage in Python*:

Since its an anti-pattern its on the decline. 

1) Proper way
```python
from threading import Lock, Thread


class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        # Now, imagine that the program has just been launched. Since there's no
        # Singleton instance yet, multiple threads can simultaneously pass the
        # previous conditional and reach this point almost at the same time. The
        # first of them will acquire lock and will proceed further, while the
        # rest will wait here.
        with cls._lock:
            # The first thread to acquire the lock, reaches this conditional,
            # goes inside and creates the Singleton instance. Once it leaves the
            # lock block, a thread that might have been waiting for the lock
            # release may then enter this section. But since the Singleton field
            # is already initialized, the thread won't create a new object.
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    value: str = None
    """
    We'll use this property to prove that our Singleton really works.
    """

    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == "__main__":
    # The client code.

    print("If you see the same value, then singleton was reused (yay!)\n"
          "If you see different values, "
          "then 2 singletons were created (booo!!)\n\n"
          "RESULT:\n")

    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()
```

2) Cheat way - a private class (_ClassName) and a function to create an instance. 
The actual instance could be stored in a global variable (bad). If its None,
the function creates an instance, saves it in the global variable and returns it,
if not None, return an instance

3) Less cheat way - lru_cache(1) or similar

---

- #### Factory Method 

Provides an interface for creating objects. The pattern suggests that we replace 
direct object construction calls (new operator or just creating an instance), with
calls to a special *factory* method/function. The factory method/function creates
it for us. 

The object creation is abstracted from the code that actually uses this
object, so modifications to the object creation etc could be done separately without
affecting, touching the code that uses it. 

Now, if dealing with classes, we could override the factory method in a subclass
and change the class of products being created by this method. So, you have a base
class, which has the factor method (interface). Child classes extend the base class
and could come up with their own implementations of this method - what they return. 

The client code, the one that uses the created object doesn't see any difference
in the objects returned as long as they implement the predefined interface.

*Applicability*:

Use the factory method when you don't know beforehand the exact types and 
dependencies of the objects your code should work with. For example, to add a new
product type to your app, you'll only need to create a new creator subclass and
override and factory method in it.

Use the pattern when you want to provide the users of your package/library/framework
with a way to extend its interval components. 

```python
from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method. + core business logic (some_operation)
    """

    @abstractmethod
    def factory_method(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass

    def some_operation(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""


class ConcreteCreator1(Creator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
  
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
Concrete Products provide various implementations of the Product interface.
"""


class ConcreteProduct1(Product):
  
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
  
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
```
^ Creator has an abstractmethod (factory method), which children can override +
some core business logic which relies on the created object. 

The client code expects a Creator, and calls some core business logic on it but
each subclass of the Creator will provide the business logic with a different
object (that sounds so stupid haha)


TODO: Complete me - https://realpython.com/factory-method-python/ 


---

### Structural patterns

--- 

### Behavioral patterns

---