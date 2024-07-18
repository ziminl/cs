# Name:Dahyun Eom
# SBUID:115943034

def checkValidInterval(sorted_lst, query):
    """ This function check if the query value can
    exist in the sorted list
    
    Args:
        sorted_lst (list)
        query (int or float)
    
    Returns:
        bool: is the query possibly in the sorted list?
    """
    return sorted_lst[0] <= query <= sorted_lst[-1]
    
def backwardLinearSearch(lst, query, max_index, min_index):
    """ This function is backward linear search applyed on lst
    in order to find the index of the query value
    the search is backward perform in the range [min_index, max_index]
    
    Args:
        lst (list)
        query (int or float)
        max_index (int)
        min_index (int)
    
    Returns:
        int: index of the query value
        return None if the value is not in list
    """
    for i in range(max_index, min_index-1, -1):
        if query == lst[i]:
            return i

def findStepSize(lst):
    """ Compute the jump step size sqrt(N)
    where N is the length of the list lst
    
    Args:
        lst (list)
    
    Returns:
        int: the ideal jump size for jump sortss
    """
    stepSize = (len(lst))**(0.5)
    return int(stepSize)

def jumpSearch(lst, query):
    """ Implementation of the jump search function
    
    Args:
        lst (list)
        query (int or float)
    
    Returns:
        int: index of the query value in the list
        return None if the value is not in list
    """
    if checkValidInterval(lst, query) is True:
        jump_size = findStepSize(lst)
        i = 0
        while query > lst[i]:
            i += jump_size
            if i > len(lst) - 1:
                return backwardLinearSearch(lst, query, len(lst) - 1, i - jump_size)
            if query <= lst[i]:
                max_index = i
                min_index = i - jump_size 
                return backwardLinearSearch(lst, query, max_index, min_index)
    return None



# ---------------------------- MAIN FCT ---------------------------------
def main():

    lst = [0,2,3,4,10,20,30,50,100,200,300,400,1000,1001]
    query = 300
    print(jumpSearch(lst, query))
    
if __name__ == "__main__": # do not mind this line, it is something we commonly use in python. You can google
    main() # Here we run the main
