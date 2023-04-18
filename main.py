import tests
from library import Library


if __name__ == '__main__':
    library = Library('library.db')
    tests.create_test_data(library)
