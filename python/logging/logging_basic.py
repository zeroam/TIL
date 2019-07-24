import logging

def word_count(myfile):
    logging.basicConfig(level=logging.DEBUG, 
        filename='myapp.log', format='%(asctime)s %(levelname)s: %(message)s')
    try:
        # count the number of words in a file and log the result
        with open(myfile, 'r') as f:
            file_data = f.read()
            words = file_data.split(" ")
            num_words = len(words)
            logging.debug("this file has %d words", num_words)
            return num_words
    except OSError as e:
        logging.error(e)
    
if __name__ == "__main__":
    word_count("myfile.txt")
    word_count("none.txt")

