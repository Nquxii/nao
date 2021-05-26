# nao.py - Never leave your terminal

Nao.py is a simple terminal program that outlines your day and displays what you need it to. Get a boost for the day and move forward with your goals
  
![basic setup of script](https://github.com/Nquxii/nao/blob/main/imgs/demo.png?raw=true)
  
  
## Setup

To get started with nao, clone this repository, change your directory into nao, and run the script like so:


```
git clone https://github.com/Nquxii/nao.py
```
```
cd nao
```
```
python3 nao.py
```

These commands should get you started.

`-n Name          ` - sets your name as 'Name'
  
`-c SCHD          ` - adds category 'SCHD'
  
`-d, 1, Math Class` - adds 'Math Class' to your SCHD category  
  
Nao uses `json` to store and grab information. if you'd like, you can skip the setup entirely and modify the json, in the same folder.


#### once you've gotten past the initial setup, you can then freely use nao and modify your configuration.


## Usage and basic commands

### here are all current commands. There are examples for clarification.


| Command | Description | Usage | Example |
| --- | ----------------------------------------------------------- | ------------------------------------------------------------------------- | ----------------- |
| x   | exit nao                                                    | x                                                                         | nao>>x            |
| q   | display another quote                                       | q                                                                         | nao>>q            |
| h   | show all nao commands                                       | h                                                                         | nao>>h            |
| t   | display the current time                                    | t                                                                         | nao>>t            |
| -n  | add (or change) your name                                   | -n                                                                        | -n Eren           |
| -t  | add another to-do to nao                                    | -t {subject}                                                              | -t Walk the dog   |
| -rt | remove a to-do from nao                                     | -rt {number of todo}                                                      | -rt 2             | 
| -c  | add a new category to nao                                   | -c {topic}                                                                | -c SCHD           |
| -rc | remove a category from nao                                  | -rc {number of user defined category}                                     | -rc 1             |
| -d  | add a description to one of your categories                 | -d, {number of user defined category}, {what you want to input there}     | -d, 2, visit gran |
| -rd | remove part of a description from one of your categories    | -rd, {number of user defined category}, {what you want to remove there}   | -rd, 2, visit gran|

#### see the 'docs' folder for more info. 
##### Thank you for viewing. I hope you find the script useful.
