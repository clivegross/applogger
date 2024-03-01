# applogger
This simple python module defines a class which implements a file based event logging system for applications. Built on the python3 `logging` module.


## Usage

```
from time import sleep
from applogger import AppLogger

logger = AppLogger(log_dir='logs', log_file='log', name='log', backup_count=30) # default values

while True:
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
    # wait for 10 seconds
    sleep(10)
```

Log directory, AppLogger will first create `log_dir` it if doesn't already exist:

```
- logs
    |- log (active log)
    |- log.2024-03-01
    |- log.2024-03-02
```

Log file content:

```
2024-03-02 08:44:21,386 - DEBUG - This is a debug message
2024-03-02 08:44:21,387 - INFO - This is an info message
2024-03-02 08:44:21,388 - WARNING - This is a warning message
2024-03-02 08:44:21,388 - ERROR - This is an error message
2024-03-02 08:44:21,389 - CRITICAL - This is a critical message
```