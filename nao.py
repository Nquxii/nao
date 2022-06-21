import json
import os
import random
import argparse
import datetime as dt

# set the config file as {current_directory}/config.json
config_file = os.path.join(os.path.dirname(__file__), 'config.json')

# open config file and define necessary variables
with open(config_file, encoding='utf-8') as f:
    config = json.load(f)

    quotes = config["quotes"]

# set argparse parser and add arguments
parser = argparse.ArgumentParser(description='Configure nao.py')

parser.add_argument('--a', type=str, help='append an item to your list')
parser.add_argument('--r', type=int, help='remove an item from your list')
parser.add_argument('--q', type=int, help='output a random quote')
parser.add_argument('--cn', type=str, help='set a name')

args = parser.parse_args()

# utilize args based on their existence
config["name"] = args.cn if args.cn is not None else config["name"]

config["list"].pop(int(args.r)) if args.r is not None else config["list"]

config["list"].append(args.a) if args.a is not None else config["list"]

quote = quotes[random.randint(0, len(quotes) - 1)]

# Dump made changes
with open(config_file, 'w', encoding='utf-8') as f:
    json.dump(config, f, indent=4)

# Set time message
time = dt.datetime.now()

if time.hour < 12:
    timeMsg = 'Good Morning'
elif 12 <= time.hour < 18:
    timeMsg = 'Good afternoon'
else:
    timeMsg = 'Good evening'

# Output messages to terminal
print(f'{timeMsg}, {config["name"]} \n')

print('[TIME]', dt.datetime.now().strftime('%m/%d/%y | %I:%M %p'))
print('[DATE]', dt.datetime.now().strftime('%A %B %d'))
print('[TODO]', ', '.join(config["list"]))

print('\n' + quote)
