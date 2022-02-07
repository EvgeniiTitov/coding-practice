### Structured concurrency and AnyIO

A way to write concurrent programs that's easier than manually taking care of 
the lifespan of concurrent tasks (hello asyncio). 

AnyIO - structured concurrency on top of asyncio + supports trio. Provides nurseries 
among other cool features poorly implemented or entirely missing in asyncio.


#### Core AnyIO features:

```commandline
- Nurseries: 
```
