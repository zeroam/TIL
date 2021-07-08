# lowermodule.py
import logging
import logging.config
import traceback

logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


def word_count(myfile):
    try:
        # count the number of words in a file, myfile, and log the result
        with open(myfile, 'r+') as f:
            file_data = f.read()
            words = file_data.split(' ')
            final_word_count = len(words)
            logger.info(f'this file has {final_word_count} words')
            f.write(f'this file has {final_word_count} words\n')
            return final_word_count
    except OSError as e:
        logger.error(e, exc_info=True)
    except:
        logger.error(f'{traceback.format_exc()}')
        return False


if __name__ == '__main__':
    word_count('myfile.txt')
    word_count('none.txt')