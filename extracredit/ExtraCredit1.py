# Name: Dahyun Eom
# SBUID: 115943034

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# -----------------         Search and sort fruits              -----------------
# TODO: Complete the implementation of listStatistic() and listStd().
# Declare a list of fruit in the main and run the code

def sort_fruits_alphabetically(fruits):
    """ This function sorts fruit by alphabetical order
    
    Args:
        fruits (list): list of fruits
    
    Returns:
        list: sorted list by alphabetical order
    """
    return sorted(fruits)

def filter_fruits_by_length(fruits, min_length):
    """ This function filter fruits by string lenth
    
    Args:
        fruits (list): list of fruits
        min_length (int): minimum length for filtering
    
    Returns:
        list: filtered list
    """
    new_list_of_fruits = []
    for i in range(len(fruits)):
        if len(fruits[i]) >= min_length:
            new_list_of_fruits.append(fruits[i])
    return new_list_of_fruits

# ---------------------------- Exercise II ---------------------------------------
# -----------------         Second-hand book E-commerce          -----------------
# TODO: Complete the implementation of searchBookTitle(), 
# bubbleSortBooks() and rangeQualityCheckBooks


import csv

def read_books_from_csv(filename):
    """ This function reads the CSV file containing
    the list of Books: Title, Price, Quality, Cover
    
    Args:
        filename (string): relative or absolute path to the csv file
    
    Returns:
        list: nested list
    """
    books = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            title, price, quality, soft_cover = row
            books.append([title, float(price), int(quality), soft_cover == 'Yes'])
    return books

def searchBookTitle(list_book, title):
    """ This function  returns all the books having the name "title"
    Args:
        list_book (list): book database
        title (string): Title of the books you are looking for
    
    Returns:
        list: nested list
    """
    new_list_base_on_tiltle = []
    for i in range(len(list_book)):
        if list_book[i][0] == title:
            new_list_base_on_tiltle.append(list_book[i])
    return new_list_base_on_tiltle

def shakerSortBooks(list_book, what_to_sort, ascending):
    '''
    This function sort book given one of its attribute (either price or quality)
    Args:
        list_book: book database
        what_to_sort : A string representing the field to sort by. i.e. "price" or "quality", otherwise (if any other string is entered) it will sort by price
        order : A bool representing the sort order. True for ascending order or False for descending order.
    '''
    if what_to_sort == "price":
        if ascending is True:
            price_list = []
            for i in range(len(list_book)):
                price_list.append(list_book[i][1])

            while price_list != sorted(price_list):
                for j in range(1, len(list_book)):
                    if list_book[j-1][1] > list_book[j][1]:
                        list_book[j-1], list_book[j] = list_book[j], list_book[j-1]
                for k in range(len(list_book)-1):
                    if list_book[len(list_book)-k-1][1] < list_book[len(list_book)-k-2][1]:
                        list_book[len(list_book)-k-2], list_book[len(list_book)-k-1] = list_book[len(list_book)-k-1],  list_book[len(list_book)-k-2]  
                price_list = []
                for l in range(len(list_book)):
                    price_list.append(list_book[l][1])

                if price_list == sorted(price_list):
                    break

        if ascending is False:
            price_list = []
            for i in range(len(list_book)):
                price_list.append(list_book[i][1])

            while price_list != sorted(price_list, reverse=True):
                for j in range(1, len(list_book)):
                    if list_book[j-1][1] < list_book[j][1]:
                        list_book[j-1], list_book[j] = list_book[j], list_book[j-1]
                for k in range(len(list_book)-1):
                    if list_book[len(list_book)-k-1][1] > list_book[len(list_book)-k-2][1]:
                        list_book[len(list_book)-k-2], list_book[len(list_book)-k-1] = list_book[len(list_book)-k-1],  list_book[len(list_book)-k-2]  
                price_list = []
                for l in range(len(list_book)):
                    price_list.append(list_book[l][1])

                if price_list == sorted(price_list, reverse=True):
                    break


    if what_to_sort == "quality":
        if ascending is True:
            price_list = []
            for i in range(len(list_book)):
                price_list.append(list_book[i][2])

            while price_list != sorted(price_list):
                for j in range(1, len(list_book)):
                    if list_book[j-1][2] > list_book[j][2]:
                        list_book[j-1], list_book[j] = list_book[j], list_book[j-1]
                for k in range(len(list_book)-1):
                    if list_book[len(list_book)-k-1][2] < list_book[len(list_book)-k-2][2]:
                        list_book[len(list_book)-k-2], list_book[len(list_book)-k-1] = list_book[len(list_book)-k-1],  list_book[len(list_book)-k-2]  
                price_list = []
                for l in range(len(list_book)):
                    price_list.append(list_book[l][2])

                if price_list == sorted(price_list):
                    break

        if ascending is False:
            price_list = []
            for i in range(len(list_book)):
                price_list.append(list_book[i][2])

            while price_list != sorted(price_list, reverse=True):
                for j in range(1, len(list_book)):
                    if list_book[j-1][2] < list_book[j][2]:
                        list_book[j-1], list_book[j] = list_book[j], list_book[j-1]
                for k in range(len(list_book)-1):
                    if list_book[len(list_book)-k-1][2] > list_book[len(list_book)-k-2][2]:
                        list_book[len(list_book)-k-2], list_book[len(list_book)-k-1] = list_book[len(list_book)-k-1],  list_book[len(list_book)-k-2]  
                price_list = []
                for l in range(len(list_book)):
                    price_list.append(list_book[l][2])

                if price_list == sorted(price_list, reverse=True):
                    break
    
    return list_book


def rangeQualityCheckBooks(list_book, quality_range):
    '''
    This function filter book within a quality range (INCLUSIVE)
    Args:
        list_book (list): book database
        quality_range (list): a list with two integer values for the beginning and end range (valid range 0-5)
    '''
    list_of_qualityRange = []
    for i in range(len(list_book)):
        if quality_range[0] <= list_book[i][2] <= quality_range[1]:
            list_of_qualityRange.append(list_book[i])
    return list_of_qualityRange

# ---------------------------- MAIN FCT ---------------------------------
def main():

    ########################
    ## Exercise 1 - Fruits ##
    # For the exercise 1 you have to declare a list of fruit
    # And call your functions by yourself
    list_of_fruits = ["apple", "banana", "orange", "kiwi", "strawberry", "grape", "mango", "blueberry", "pineapple", "watermelon"]
    print(sort_fruits_alphabetically(list_of_fruits))
    print(filter_fruits_by_length(list_of_fruits, 6))

    ## Exercise 2 - Books ##
    books = read_books_from_csv('./Books.csv')

    # 1. Search for Harry Potter books
    title = "Harry Potter"
    book_search = searchBookTitle(books, title)
    print("We can find " + str(len(book_search)) + \
          " books called " + title + " in the database ")

    # 2. Sort your book by price using bubble sort
    shakerSortBooks(book_search, "price", True)

    # 3. return only the book with the quality in a given range
    quality_range = [3,5]
    accepted_books = rangeQualityCheckBooks(book_search, quality_range)

    # Display the books
    for book in accepted_books:
        print(book)

if __name__ == "__main__": # do not mind this line, it is something we commonly use in python. You can google
    main() # Here we run the main
