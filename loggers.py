import logging

"""
Logging Levels

DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

logging.basicConfig(level=logging.DEBUG)
handler = logging.FileHandler("mylog.log")
handler.setLevel(logging.INFO)

logging.warning("You have got 20 mails")
logging.critical("All components failed")
logging.info("Information here")

formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler.setFormatter(formatter)
# ------------------ Creating my own logger ---------------------------------

logger = logging.getLogger("Intermediate Python")
logger.addHandler(handler)
logger.info("Logger Created by me")
logger.critical("Your channel deleted")
logger.log(logging.ERROR, "An error occured")
logger.debug("Debugging your code")
logger.setLevel(logging.DEBUG)


logger.info("IMPORTANT INFORMATION")