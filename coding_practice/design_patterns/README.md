#### TODO:

- https://refactoring.guru/design-patterns/catalog

---

#### General info:

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

#### Summaries:


- Facade design pattern

A facade is an object that serves as a front-facing interface masking more complex
underlying or structural code. The pattern hides the complexities and provides a 
simpler interface to the client.

An example could be a class that implements, say, 
linked list functionality (insertion, deletion, etc), it hides all the complicated
logic inside exposing clean and simple interface.

Different from the Adapter pattern, which converts one interface to another so that
ot matches what the client expects. 

--- 