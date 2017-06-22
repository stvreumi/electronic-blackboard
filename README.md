# Electronic Blackboard [![Build Status](https://travis-ci.org/SWLBot/electronic-blackboard.svg?branch=master)](https://travis-ci.org/SWLBot/electronic-blackboard) 

This project is a electronic bulletin board of broadcasting images and announcement templates by web browser. The system provides broadcast scheduling, wieldy user interface for uploading and mutiple automated functions.  

The functions Electronic-Blackboard included are as follows
* Customized scheduling mode selection
* CWB crawler for weather radar image
* Google calendar
* Announcement template
* etc

## Setup

### Prerequisites

Since the project is totally written in python 3, pyhton 2 is not recommended.
* Python3
* MySQL

### Installing

1. For the libraries needed
```
# pip3 install -r requirements.txt
```
2. create nessasary files in this project
  * create `mysql_auth.txt`
3. The content inside `mysql_auth.txt` should be  
  * Host
  * User
  * Password
  * Database  -create the database first where to store your data
```
localhost
root
your_password
yout_database_name
```
4. Execute `env_init.py` to automatically initialize environment settings
```
$ python3 env_init.py
```

## Run test
`$ python3 test/test.py`
if success, it should print
```
test_close (test_mysql.Mysql) ... ok
...
test_set_schedule_log (test_arrange_schedule.Arrange_Schedule) ... ok
----------------------------------------------------------------------
Ran 12 tests in XXX.XXs

OK
```

## Start
```
$ python3 server.py
$ python3 arrange_schedule.py
$ python3 board.py
```

Open the web browser to check the implement result with the url `localhost:3000` and `localhost:4000`
* port:3000 -the platform of uploading files
* port:4000 -the broadcast display



