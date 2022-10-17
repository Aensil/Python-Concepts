# import math module
import math

def run():
    #Dictionary comprenhensions
    list_dict = {i: i**3 for i in range(1,101) if i % 3 != 0}

    #print(list_dict)

    #challenges
    dict_x ={i: math.sqrt(i) for i in range(1,1001)}
    print(dict_x)



if __name__ == '__main__': #Entry Point
    run()