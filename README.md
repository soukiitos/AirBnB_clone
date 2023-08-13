# 0x00.AirBNB_clone - The console

![AirBnB clone](https://thedesignlove.com/wp-content/uploads/2019/07/Features-of-a-Good-Logo-Design-01-1024x750.jpg){width="250px"}

## Description of the project

### Resources
[cmd module](https://intranet.alxswe.com/rltoken/8ecCwE6veBmm3Nppw4hz5A)
[cmd module in depth](https://intranet.alxswe.com/rltoken/uEy4RftSdKypoig9NFTvCg)
[packages concept page]
[uuid module](https://intranet.alxswe.com/rltoken/KfL9TqwdI69W6ttG6gTPPQ)
[datetime](https://intranet.alxswe.com/rltoken/1d8I3jSKgnYAtA1IZfEDpA)
[unittest module](https://intranet.alxswe.com/rltoken/IlFiMB8UmqBG2CxA0AD3jA)
[args/kwargs](https://intranet.alxswe.com/rltoken/C_a0EKbtvKdMcwIAuSIZng)
[Python test cheatsheet](https://intranet.alxswe.com/rltoken/tgNVrKKzlWgS4dfl3mQklw)
[cmd module wiki page](https://intranet.alxswe.com/rltoken/EvcaH9uTLlauxuw03WnkOQ)
[python unittest](https://intranet.alxswe.com/rltoken/begh14KQA-3ov29KvD_HvA)

### Requirements

#### Python Scripts
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all the files should be exactly #!/usr/bin/python3
- The code should use the pycodestyle (version 2.8.*)
- All the files must be executable
- The length of the files will be tested using wc
- All the modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All the classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All the functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

#### Python Unit Tests
- Allowed editors: vi, vim, emacs
- All files should end with a new line
-  All test files should be inside a folder tests
- Must use the [unittest module](https://intranet.alxswe.com/rltoken/op1-rQGlw0wwwqNBsn1yaw)
- All test files should start by test_
- All tests should be executed by using this command: python3 -m unittest discover tests
- Can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
- All modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

## More Info

### Execution

###### The shell we should work like this in interactive mode
$ ./console.py
(hbnb) help

##### Documented commands (type help <topic>):
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

###### But also in non-interactive mode
$ echo "help" | ./console.py
(hbnb)

##### Documented commands (type help <topic>):
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

##### Documented commands (type help <topic>):
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
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 

### Commands
- Create:
create BaseModel
- All:
all BaseModel
- Show:
show BaseModel
- Destroy:
destroy
- Count:
count
- Update:
update BaseModel

## AUTHORS

- Fouad Yasin
- Soukaina Lachheb
