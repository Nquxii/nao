import datetime
import linecache
import random
import sys
import json

# Help Commands
helpn = '''
Type -t [topic] to add a to-do.

Type -rt [number] to remove a to-do.

Type -c [topic] to add an entire category to nao.

Type -rc [line of user defined category] to remove an entire category from nao.

Type -d, [line of user defined category], [description] to add a description.

Type -rd, [line of user defined category], [description]

Type -n [name] to add/change your name

Type h to view nao's commandlist.

Type t to view the time.

Type q to view another quote.

Type x to exit nao.
'''

# Number increment command
def inc():
    global incr
    incr = incr + 1

# Main json file path (important to change for usage convinience)
jsonFile = open('userfile.json')
data = json.load(jsonFile)

# update json function
def jsu():
    jsonFile = open("userfile.json", "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()

# Add another todo
def add_todo(i):
    i = i.removeprefix('-t ')
    to_do = data["todo"]

    if to_do == "" or to_do == " ":
        to_do = i
    else:
        to_do = to_do + ', ' + i
    data["todo"] = to_do

# Remove a todo
def rem_todo(i):
    i = i.removeprefix('-rt ')
    to_do = data["todo"]

    to_do = to_do.split(', ')

    to_rem = to_do[-1 + int(i)]

    if ', ' + to_rem in data["todo"]:
        to_rem = ', ' + to_rem
    elif to_rem + ', ' in data["todo"]:
        to_rem = to_rem + ', '
    else:
        print('\nno such value.\n')

    data["todo"] = (data["todo"]).replace(to_rem, '')

# Add another category
def add_category(i):
    i = i.removeprefix('-c ')
    if data["categories"] == '' or data["categories"] == ' ':
        cate = i
    else:
        cate = data["categories"] + ', ' + i
    data["categories"] = cate

# Remove a category
def rem_category(i):
    i = i.removeprefix('-rc ')

    if ', ' in data["categories"]:
        index = int(i) + -1
        cat = (data["categories"]).split(', ')
        to_rem = ', ' + cat[index]
        data["categories"] = (data["categories"]).replace(to_rem, "")
        data['cat' + str(index)] = ''

    else:
        data["categories"] = ''

def add_description(i):
    i = i.removeprefix('-d, ')
    i = i.split(', ')
    i[0] = int(i[0]) - 1
    sec = 'cat' + str(i[0])
    data[sec] = str(i[1])

def rem_description(i):
    i = i.removeprefix('-rd, ')
    i = i.split(', ')
    i[0] = int(i[0]) - 1

    sect = 'cat' + str(i[0])

    (data[sect]).replace(i[1], '')

# display extra categories
incr = 0
def cate():
    if ', ' in data["categories"]:
        sects = (data["categories"]).split(', ')
        inc()

        increm = -1 + incr
        sec = 'cat' + str(increm)

        if sects[increm] == '' or sects[increm] == ' ':
            pass

        else:
            try:
                print('[' + sects[int(increm)] + ']', data[sec])
                jsu()
                cate()
            except IndexError:
                pass
    else:
        sects = (data["categories"]).split(', ')
        inc()
        sec = 'cat' + str(-1 + incr)

        if data["categories"] == '' or data["categories"] == ' ':
            pass
        else:
            print('[' + data["categories"] + ']', data[sec])


# Nao arguments
def com():
    i = str(input('\nnao >>'))
    if i == 'x':
        print('Sayonara.')
        sys.exit()
    elif i == 'q':
        quote()
    elif i == 'h':
        print(helpn)
    elif i == 't':
        print(datetime.datetime.now().strftime('%I:%M %p'))
    elif i.startswith('-t '):
        add_todo(i)
    elif i.startswith('-rt '):
        rem_todo(i)
    elif i.startswith('-c '):
        add_category(i)
    elif i.startswith('-rc '):
        rem_category(i)
    elif i.startswith('-d, '):
        add_description(i)
    elif i.startswith('-rd, '):
        rem_description(i)
    elif i.startswith('-n '):
        i = i.removeprefix('-n ')
        data["name"] = i
    jsu()
    com()

print('''
»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
                                      nao
«««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««
''')

time = datetime.datetime.now()
if time.hour < 12:
    time = 'Good Morning,'
elif 12 <= time.hour < 18:
    time = 'Good afternoon,'
else:
    time = 'Good evening,'
print(time, data["name"] + '\n')

quote = linecache.getline('quotes.txt', random.randint(1, 50))
print(quote + '\n')

print('[TIME]', datetime.datetime.now().strftime('%m/%d/%y | %I:%M %p'))

print('[DATE]', datetime.datetime.now().strftime('%A %B %d'))

print('[TODO]', data["todo"])

cate()
com()
