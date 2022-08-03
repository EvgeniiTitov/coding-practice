### General info:

Design patterns are usually split into 3 categories:

- Creational Patterns
  
  - Deal with the creation (construction) of objects
  - Explicit (constructors) vs implicit (DI, reflection, etc)
  - Wholesale (single statement) vs picewise (step-by-step)

- Structural Patterns

  - Concerned with the structure (class members, etc)
  - Many patterns are wrappers that mimic the underlying class's interface
  - Stress the importance of good API design

- Behavioural Patterns

  - All quite different, no central theme

---

###Summary:


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