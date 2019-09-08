import logging
 #Create and configure logger
logging.basicConfig(filename="newfile.log", format='%(asctime)s %(message)s', filemode='w')
 #Creating an object
logger=logging.getLogger()
 #Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)
#Test messages
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")

import logging
LOG_FILENAME = 'newfile.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

logging.debug('This message should go to the log file')