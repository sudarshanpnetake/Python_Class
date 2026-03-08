import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# case 1
handler1 = logging.FileHandler("file1.log", mode="a")
handler1.setLevel(logging.DEBUG)

# case 2
handler2 = logging.FileHandler("file2.log", mode="a")
handler1.setLevel(logging.INFO)

formatter= logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
formatter2= logging.Formatter('%(levelname)s - %(message)s')

handler1.setFormatter(formatter)
handler2.setFormatter(formatter2)

logger.addHandler(handler1)
logger.addHandler(handler2)

logger.debug("This is debug messgae")
logger.info("This is info messgae")
logger.error("This is error messgae")
