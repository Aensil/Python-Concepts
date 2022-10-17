#Import function reduce
from functools import reduce

def run():
    #High order functions
    #FILTER functions
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]

    odd = list(filter(lambda x: x%2 != 0, my_list))
    squares = list(map(lambda x: x**2, my_list))
    all_multiplied = reduce(lambda a, b: a * b, my_list)

    print("Filter Odd functions: " , odd)
    print("Map squares functions: ", squares)
    print("Reduce multiplied functions: ", all_multiplied)



if __name__ == '__main__': #Entry Point
    run()