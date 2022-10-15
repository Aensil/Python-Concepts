def run():
    #list of 100 firs numbers /3 which are feasible
    #LIST COMPREHENSIONS
    list_test = [i**2 for i in range(1, 101) if i % 3 != 0]
    
    print(list_test)

    #Challenge
    #Multiples of 4 and 6 and 9 until 9999
    list_x = [i for i in range(1, 10000) if ((i % 4 == 0) and (i % 6 == 0) and (i % 9 == 0))]

    print(list_x)


if __name__ == '__main__': #Entry Point
    run()