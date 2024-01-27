import sys


def search_and_replace(path: str = '', search: str = '', replace: str = ''):
    """Replace searched word in the file from the path."""
    with open(path, 'r') as file:
        file_contents = file.read()

        updated_contents = file_contents.replace(search, replace)

    with open(path, 'w') as file:
        file.write(updated_contents)


# To call the function with parameters from cmd add: file path, search world and replace world
# example: py -3 replace.py plik.txt ServerName=Server2 ServerName=Server77
search_and_replace(sys.argv[1], sys.argv[2], sys.argv[3])
