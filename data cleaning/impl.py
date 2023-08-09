import sys
import logging


def predict(name,age,sex,disease):
    log_filename="predict.log"
    log_level=logging.DEBUG
    log_format=" %(asctime)s -%(levelname)s - %(message)s"
    logging.basicConfig(filename=log_filename,level=log_level,format=log_format)
    output=print(name,age,sex,disease)
    logging.debug(output)
    return output

