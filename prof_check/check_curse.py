import urllib
"""
high level support for doing this and that.
"""
def read_text():
    """Illustrate class-level docstring."""
    file_path = "C:\Users\Benjamin\Documents\Code\learn_python\quotes.txt"
    quotes = open(file_path)
    contents_of_file = quotes.read()
    quotes.close()
    check_words(contents_of_file)

def check_words(text):
    """ Check for curse words in file """
    connection = urllib.urlopen("http://www.purgomalum.com/service/containsprofanity?text=" + text)
    output = connection.read()
    print output
    connection.close()

read_text()
