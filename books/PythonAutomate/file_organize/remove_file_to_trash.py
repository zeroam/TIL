import send2trash

bacon_file = open('bacon.txt', 'a')  # creates the file
bacon_file.write('Bacon is not a vegetable')
bacon_file.close()

send2trash.send2trash('bacon.txt')
