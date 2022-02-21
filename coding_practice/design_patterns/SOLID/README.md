### SOLID:

### 1. Single Responsibility Principle (SRP) / Separation of Concerns (SOC)

Easier to implement, prevents unexpected side-effects of future changes. 

Requirements change over time. Each of them changes the responsibility of at 
least one class --> The more responsibilities your class has, the more often
you need to change it --> If your class implements multiple responsibilities, 
they are no longer independent of each other. 

Classes, software, microservices that have only one responsibility are easier
to explain, understand and implement than the ones that provide a solution for
everything.



### 2. Open-Closed Principle (OCP)

New functionality must be added by extension not modification. Open for extension, 
closed for modification.


### 3. Liskov Substitution Principle (LSP)

An overriden method of a subclass needs to accept the same input parameter 
values as the method of the superclass. Signatures match.

When you have an interface accepting some base class as its parameter, 
we must be able to provide any of the base class inheritors without breaking 
anything. 


### 4. Interface Segregation Principle

Intead of having one large interface specifying a whole bunch of methods (
that might not all apply to the entities implementing this interface) keep
things more granular --> have multiple interfaces encapsulating certain logic 
or behaviour. If an entity needs this one large interface, it just implements
all smaller interfaces.

### Dependency Inversion Principle

High level classes or modules should not depend on low level modules/classes,
instead they need to depend on abstractions (interfaces abstracting away low 
level details, so that things are pluggable and could be changed). 
Say you have a low level class that stores some info in a list, the high level
class using this low level class relies on the list syntax to get items from
the low level object. Then, we replace the low level object with a different one
storing items in a dictionary. Now the high level classes is fucked as it relies
on the list syntax --> needs to be modified. 


Use interfaces, logic should be moved to low level objects implementing certain
interface, so that the high level objects could just consume it without caring
how its done under the hood.

To reiterate, high level objects rely on interfaces that are implemented by
the lower level obejcts. As a result, low level objects could be swapped out 
without having to modify the high level objects. Feelsgoodman been doing it 
for a while now.