https://refactoring.guru/design-patterns/builder

Some objects are simple and can be easily created - just call the consturctor. 
Others, on the other hand, might require a lot of ceremony to create - having
an object with 10 parameters is not productive --> piecewise constructor.

Builder - provides an API to initialize an object step by step, succinctly.

Often, it has a single creation method and several methods to configure the
resulting object: 

```someBuilder.setValueA(1).setValueB(2).create()```

Say, you have an object that could potentially have many variations. You could

    a) Create a bunch of subclasses each representing a certain variation --> leads
    to endless breeding of your subclasses

    b) Have a single class with huge constructor that receives a bunch of parameters
    that determine this object --> the most of the parameters will be unused, because
    only a subset of them is required to instantiate each object variation.

The solution:

Extract the object construction code out of its own class and move it to a 
separate objects - builders. The pattern organizes consturction into a set of
steps. To create an object, you execute a series of these steps on a builder
object. IMPORTANT - we don't need to call all of them, we call just a subset 
necessary to produce the desired configuation of an object.

Some of the construction steps might require different implementation --> Multiple
builder classes could be used. They implement the same set of building steps but
do it in different manner. These builders then can be used in the construction
process. --> The result of calling a set of the same methods on different builders 
will result in different objects.

Builders must be abstracted away, so that the clients using the builders could 
work with them in the unified manner --> Director. 

You can go further and extract a series of calls to the builder steps you use 
to construct a product into a separate class called director. The director 
class defines the order in which to execute the building steps, while the 
builder provides the implementation for those steps.

Having a direction is optional, a client could always just call the building 
steps in a specific order directly. Having a director, on the other hand, allows
to completely hide the details of product consturction from the client code. 
The client only needs to associate a builder with a director and launch the 
construction with the director. 