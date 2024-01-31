import sys


def search_and_replace(path: str = '', search: str = '', replace: str = ''):
    """Replace searched word in the file from the path."""
    try:
        with open(path, 'r') as file:
            file_contents = file.read()
            updated_contents = file_contents.replace(search, replace)
    except FileNotFoundError:
        print(f'File "{path}" not found')
        exit()

    with open(path, 'w') as file:
        file.write(updated_contents)

    with open(path, 'r') as file:
        file_contents = file.read()
    if search in file_contents:
        print('Something went wrong')
    else:
        print('All done')


try:
    search_and_replace(sys.argv[1], sys.argv[2], sys.argv[3])
except IndexError:
    print("""To call the function with parameters from cmd add: file path, search world and replace world
example: py -3 replace.py plik.txt old new""")
    exit()
