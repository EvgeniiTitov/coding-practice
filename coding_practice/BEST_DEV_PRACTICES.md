#### Software development *best* practices (with a pinch of salt):

- YAGNI (you aint gonna need it)
    - Do you really need it?
    - Simpler way?
    - Reuse pre-existing work
    - Do not reinvent the wheel
    
---

- KISS (keep it simple stupid)
    - Favor simplicity in design and code
    - Patterns should benefit the code (don't just add them because you want to)
    - Iteratively simplify code
    
---
 
- DRY (do not repeat yourself)
    - helper/utils package for code you keep rewriting over and over
    - Modularize and reuse your code  
        - Break large chunks of code into functions
        - Group relevant functions into modules/classes
        - Group relevant modules/classes into packages
        - Publish packages as libraries    
    - Use existing libraries

---
        
- Single Responsibility Principle (SRP)
    - One function - one functionality
    - One class - one purpose
    - One library/package - one responsibility (numpy doesn't allows http calls)

---
        
- Separation of Concerns (broader than SRP)
    - Design your program per concern - say we get data from the server, validate, display it. Those could be
        separate into 3 layers: communication later, validation, UI. Each has
        a specific job. You don't mix UI code with communication layer etc.

---
        
- Composition Over Inheritance
    - Instantiate instead of inheriting OR at least aggregate
    - Inheritance if overused complicates things substantially

---

- Dependency Injection
    - Instances of objects an object needs get passed as arguments, it doesn't instantiate
    them itself.
    - Callers handle dependencies
    - Concern of instantiating dependencies is separated
    - Too many input params is a sign your code is doing too much.

---

- Interfaces
    - Your objects should depend on interfaces rather than actual class 
    implementations (loose coupling)

---
 
- Fail fast
    - Check input and fail on nonsensical input or invalid state early in your 
    program

---

- Self documenting code through good naming practices
    - Variables/Classes: nouns
    - Functions/methods: verbs
    - Parameters/arguments should explain what they represent, not X, Y, array, etc

---

- Test-Driven Development
    - Clearly identify the objective and requirements. Come up with tests. Start writing
    code to pass those tests. Add more relevant tests (edge cases, exceptions such as
    incorrect input) etc.

---

- Write defensively: always think what could go wrong, what might fail, invalid input etc,
will help to catch more bugs before they happen.

---

- Stateless and side effect free functions are easier to test. Alternatively, separating
stateful code and code with side-effects into smaller functions makes them easier to mock
out

---

- One way communication data flow
    - Objects communicate top-to-bottom or one-way, easier to debug and catch issues.
    - Communication busses
   