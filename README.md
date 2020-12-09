# Rock, Paper, Scissor, Lizard, Spock game 

A classic game to settle out disputes or cure for extreme boredom. It is recommended that you actually do not play this game via an API. Instead find a friend or go out an grab any stranger to play with. 

## How to use:

You can play with "hand" or change mode/reset score with "mode" through a POST request. In advanced mode you can additionaly play with SPOCK and LIZARD hands.

```json
      {"hand": "ROCK/PAPER/SCISSORS etc."}
      or
      {"mode": "CLASSIC/ADVANCED"}
```
example 
``` 
$ curl -X POST localhost:4567/game -d '{"hand": "paper"}' 
or
$ curl -X POST localhost:4567/game -d '{"mode": "advanced"}'

```

You can also get the score with a plain GET request.

## Rules:

In case you do know the rules here is what beats what.
```

{ "scissors": ("paper","lizard"),
  "paper": ("rock", "spock"),
  "rock" : ("lizard", "scissors),
  "lizard": ("spock", "paper"),
  "spock": ("scissors", "rock")
}
```
