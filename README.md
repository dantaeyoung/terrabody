
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

The ether is treated like a cytoplasm. Messages move back and forth. 

terraprograms are crafted on top of terrabody.

## implementation

ZeroMQ is used as a messaging system to exchange messages between organs. 

Pros:
- Each organ (computing module) operates individually.
- You can interject and 'hook' into any particular organ's functions from external processes, including the webui.

Cons:
- Chasing down program flow is a bit like following a white rabbit, or understanding the Krebs cycle.

## message format

`FROM--to--TO::MESSAGE:::PAYLOAD`
`openai--to--piper::say:Hello! I'm just a digital assistant, so I don't have feelings, but I'm here and ready to assist you. How can I help you today?`

<!---

```
{ 
  "from": "organ A",
  "to": "organ B", // optional 
  "subject": "received",
  "data": obj, // optional
}
```
Example 1: from GPIO broadcasting a button push

```
{ 
  "from": "gpio",
  "subject": "button1_held",
}
```
Example 2: from whisper.cpp transcribing message

```
{ 
  "from": "whisper",
  "subject": "transcribed",
  "data": {
    "text": "Hello world!".
  }
}
```
Example 3: a request to piper to vocalize a message
```
{ 
  "from": "webui",
  "to": "piper",
  "subject": "vocalize",
  "data": {
    "text": "Hi! How are you?".
  }
}
```
NOTE: `zmq_switchboard` will automatically add timestamps.
-->
## setup

See [SETUP.md](SETUP.md).
