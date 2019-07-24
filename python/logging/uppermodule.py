import logging
import lowermodule

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)


def record_word_count(myfile):
    logger.info("starting the function")
    try:
        word_count = lowermodule.word_count(myfile)
        with open('wordcountarchive.csv', 'a') as file:
            row = str(myfile) + ',' + str(word_count)
            file.write(row + '\n')
    except:
        logger.warning('could not write file %s to destination', myfile)
    finally:
        logger.debug('the function is done for file %s', myfile)


if __name__ == "__main__":
    record_word_count("README.md")
    record_word_count("myfile.txt")
