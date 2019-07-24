import logging.config
import traceback
import time

logger = logging.getLogger(__name__)
logging.config.fileConfig('logging2.conf', disable_existing_loggers=False)


def word_count(myfile):
    try:
        starttime = time.time()
        with open(myfile, 'r') as f:
            file_data = f.read()
            words = file_data.split(' ')
            final_word_count = len(words)
            endtime = time.time()
            duration = endtime - starttime
            logger.info(f'this file has {final_word_count} words', extra={'run_duration': duration})
    except OSError as e:
        logger.error(e, exc_info=True)
    except:
        logger.error(f'{traceback.format_exc()}')
        return False


if __name__ == '__main__':
    word_count('myfile.txt')
    word_count('none.txt')
