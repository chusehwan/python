def count_words(filename):
    """count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print ("The file " + filename + " has about " + str(num_words) + "words.")

filenames = ['alice.txt','little_women.txt','moby_dick.txt','siddhartha.txt']

for filename in filenames:
    count_words(filename)
