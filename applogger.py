import logging
from logging.handlers import TimedRotatingFileHandler
import os

class AppLogger:
    """
    A class used to create a file based logger. The logger will create a log file in the specified directory and will rotate the log file every day. The number of backup files to keep is configurable.

    Directory:    
    - logs
        - log
        - log.2024-03-01
        - log.2024-03-02

    Log:
    2024-03-02 08:44:21,389 - CRITICAL - This is a critical message
    2024-03-02 08:44:31,399 - DEBUG - This is a debug message
    2024-03-02 08:44:31,403 - INFO - This is an info message

    Attributes
    ----------
    logger : Logger
        a logging.Logger instance.
    handler : Handler
        a logging.Handler instance, specifically a TimedRotatingFileHandler.

    Methods
    -------
    debug(message), info(message), warning(message), error(message), critical(message)
        Logs a message with the given level.
    """
        
    def __init__(self, log_dir='logs', log_file='log', name='log', backup_count=30):
        """
        Constructs all the necessary attributes for the AppLogger object.

        Parameters
        ----------
            log_dir : str, optional
                Directory for the log files (default is 'logs2')
            log_file : str, optional
                Name of the log file (default is 'log')
            backup_count : int, optional
                Number of backup files to keep (default is 30)
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # Create the logs directory if it doesn't exist
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Define log file path
        self.log_file = os.path.join(log_dir, log_file)

        # Create a rotating file handler
        self.handler = TimedRotatingFileHandler(self.log_file, when='midnight', interval=1, backupCount=backup_count)

        # Define log format
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(formatter)

        # Add the handler to the logger
        self.logger.addHandler(self.handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    def shutdown(self):
        """
        Performs an orderly shutdown by flushing and closing all handlers.
        This method should be called at application exit and no further use of the logging system should be made after this call.
        """
        self.handler.close()
        logging.shutdown()

if __name__ == "__main__":
    # Example usage:
    logger = AppLogger()
    logger.debug('Debug message')
    logger.info('Info message')
    logger.warning('Warning message')
    logger.error('Error message')
    logger.critical('Critical message')
    logger.shutdown()
