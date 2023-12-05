
# (t e r r a b o d y)

A terrabody is a computer for a wizard. 

part of the (t e r r a) system.



## concept

Terrabody is a Body With Organs. 

An Organ has a particular function. It receives input, chews on it, digests, and then spits it out into an output. 

Each organ listens. 
If it receives a request, it chews and digests, then replies. 
Sometimes, it occasionally announces, like burping into the air. 
Sometimes, it requests something from another organ in order to chew better. 

Organs are pretty independent. Anything about an internal state, it burps. If it wants something specific to happen, it requests. 



## implementation

ZeroMQ is used as a messaging system to exchange messages between organs. The ether is treated like a cytoplasm. Messages move back and forth.

Pros:
- Each organ (computing module) operates individually.
- You can interject and 'hook' into any particular organ's functions from external processes, including the webui.

Cons:
- Chasing down program flow is a bit like following a white rabbit.


## setup

See [SETUP.md](SETUP.md).
