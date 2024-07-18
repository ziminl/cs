# Name: Dahyun Eom
# SBUID: 115943034
#******************************Score***************************
#  good --> Score: 8/10
#**************************************************************
# Remove the ellipses (...) when writing your solutions.
###--> these are some of my realizations that I got from the error I've been through.
##--> questions for tutor
#--> my mention of change in given main function(line111, please look up for it.)
# Prof. Rameau: Sorry for disturbing just a test for marking!
# Test2 for scoring
# ---------------------------- Exercise I ---------------------------------------
# ----------------- Extract statistical information from a list -----------------
# TODO: Complete the implementation of listStatistic() and listStd().

def listStatistic(list_in):
    minimum = min(list_in)                                   ###cannot write min = min(list_in)  -> yes you cant use min max functions :-1
    maximum = max(list_in)

    sum = 0
    average = 0
    for i in list_in:
        sum += (i)
    average =  sum / int(len(list_in))                       ###cannot write sum =  sum / int(len(list_in)) ; sum  = average --> sum이 0으로 초기화 되버림 
   
    return maximum, minimum, average


def listStd(list_in):
    sum = 0
    for i in list_in:
        sum += (i)
    average =  sum / len(list_in)
    
    numerator = 0
    denominator = len(list_in) - 1
    for j in list_in:
        numerator += (j - average)**2
    StandardDeviation = (numerator / denominator)**(0.5)

    return StandardDeviation


# ---------------------------- Exercise II --------------------------------------
# -----------------         Implement the Lunh Algorithm        -----------------
# TODO: Complete the implementation of reverseList(), doubleOddIndex()
# digitSum(), replaceDoubleDigit(), isCardValid() and lunhAlgorithm()

def reverseList(list_in):
    list_in.reverse()        # you cant use reverse methods, need to implemnt it yourself:-1                               ##왜 a = list_in.reverse() 하고 return a 하면 안 될까?
    return list_in


def doubleOddIndex(list_in):
    for i in range(0,16):                                    
        if i % 2 == 0:
            list_in[i] = list_in[i]*1   
        else:
            list_in[i] = list_in[i]*2
    return list_in                                             ###if write --> return reverseList(list_in)--> [8, 0, 0, 0, 0, 0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 9]

def digitSum(value):
    a = int(value) // 10
    b = int(value) % 10
    result = a + b
    return result

def replaceDoubleDigit(list_in):
    for i in range(0, 16):
        list_in[i] = digitSum(list_in[i])                       ##why cannot write ; for i in list_in ; i = digitSum(i) ; return list_in ?
    return list_in

def isCardValid(list_in):
    sum = 0
    for i in list_in:
        sum += i
    return sum % 10 == 0
        
def lunhAlgorithm(card_nb):
    a = reverseList(card_nb)
    b = doubleOddIndex(a)
    c = replaceDoubleDigit(b)
    d = isCardValid(c)
    return d

# ---------------------------- MAIN FCT ---------------------------------
def main():

    #Exercise 1 main
    my_list = [1, 2, 3, 4, 5, 6]
    list_max, list_min, list_average = listStatistic(my_list)
    print("The max of the list is: ", list_max)
    print("The min of the list is: ", list_min)
    print("The average of the list is: ", list_average)
    list_std = listStd(my_list)
    print("The std of the list is: ", list_std)

    #Exercise 2 main
    card_number = [4, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9]

    ''' Step-by-step tests (you can remove these  tests when you
    are done with the final function lunhAlgorithm )
    '''
    print("Here is the original card number: ", card_number)
    reversed_card_nb = reverseList(card_number)
    print("Here is the reversed card number: ", reversed_card_nb)
    lunh_product = doubleOddIndex(reversed_card_nb)
    print("One in two element is multipled by 2: ", lunh_product)
    print("Sum the digit in a number: ", digitSum(18))
    single_digit_prod = replaceDoubleDigit(lunh_product)
    print("Replace the double digits in the vector: ", single_digit_prod)
    validity = isCardValid(single_digit_prod)
    print("Is the card valid??", validity)

    # execute the final code
    card_number = [4, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9]   #I had to declare list car_number 1 more time because the list changed through the previous codes!
    print("Is the card valid??", lunhAlgorithm(card_number))

# Run the main code
main()
