# 0x00.AirBNB_clone - The console
### Resources

### Requirements
#### Python Scripts
#### Python Unit Tests
### More Info
#### Execution
###### The shell we should work like this in interactive mode:

$ ./console.py
(hbnb) help

##### Documented commands (type help <topic>):
##### ========================================

EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

###### But also in non-interactive mode:

$ echo "help" | ./console.py
(hbnb)

##### Documented commands (type help <topic>):
##### ========================================

EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

##### Documented commands (type help <topic>):
##### ========================================

EOF  help  quit
(hbnb) 
$

### Installation

git clone https://github.com/Vanbasten01/AirBnB_clone.git

### Testing

###### All tests should also pass in non-interactive mode

python3 -m unittest discover tests

#### Python unittest

. unittest module
. File extension .py
. Test Files start with test_
. Organization: unit tests in:... for mobels/base_model.py
### Usage

. Start the console:
$ ./console.py
(hbnb)
. Use help:
(hbnb) help

##### Documented commands (type help <topic>):
##### ========================================

EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 
### Commands

- Create
create BaseModel
- All
all BaseModel
- Show
show BaseModel
- Destroy
destroy
- Count
count
- Update
update BaseModel
## AUTHORS

- Fouad Yasin
- Soukaina Lachheb
