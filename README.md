# nao.py - Never leave your terminal

Nao.py is a simple terminal program that outlines your day and displays what you need it to. \
Get a boost for the day and move forward with your goals.

![setup of script](https://github.com/Nquxii/nao/blob/main/img/demonstration.png?raw=true)
  
## Setup

To get started with nao, clone this repository, change directory into nao, and run the script like so:

```
git clone https://github.com/Nquxii/nao.py && cd nao
```
```
python3 nao.py -h 
```

These commands should get you started.

Nao uses `json` to store and grab information. if you'd like, you can skip the setup entirely and modify the json, in the same folder.
once you've gotten past the initial setup, you can then freely use nao and modify your configuration.


## Usage

here are all current commands. There are examples for clarification.

| Command | Description | Usage | Example |
|------| ----------------------------------------- | ------------------------------------------------------------------------- | ----------------- |
| h    | show all nao commands                     | -h                                                                        | -h                |
| --n  | add (or change) your name                 | --n                                                                       | --n Mikasa        |
| --a  | add another to-do to nao                  | --a [subject]                                                             | --t Learn vim     |
| --r  | remove a to-do from nao                   | --r [index  ]                                                             | --r 2             | 


Thank you for viewing. I hope you find the script useful.
