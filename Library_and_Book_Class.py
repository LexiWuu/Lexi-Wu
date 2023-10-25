class Library:
    def __init__(self, item_name, author, publisher):
        self.__item_name = item_name
        self.__author = author
        self.__publisher = publisher

    # The following methods are mutators for the
    # class's data attributes.

    def set_item_name(self, item_name):
        self.__item_name = item_name

    def set_author(self, author):
        self.__author = author

    def set_publisher(self, publisher):
        self.__publisher = publisher

    # The following methods are the accessors
    # for the class's data attributes.

    def get_item_name(self):
        return self.__item_name

    def get_author(self):
        return self.__author

    def get_publisher(self):
        return self.__publisher


class Book(Library):
    def __init__(self, item_name, author, publisher, pages, version):
        # Call superclass __init__ method
        Library.__init__(self, item_name, author, publisher)

        # Initialize the cust_number and on_list attributes
        self.__pages = pages
        self.__version = version

    # Mutator functions for cust_number and on_list
    def set_pages(self, pages):
        self.__pages = pages

    def set_version(self, version):
        self.__version = version

    # Accessor functions for cust_number and on_list
    def get_pages(self):
        return self.__pages

    def get_version(self):
        return self.__version
