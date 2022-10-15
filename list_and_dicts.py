def run():
    my_list = [1, "Hello", 4.5]
    my_dict = {"firstname": "Enoc", "lastname":"Awesome"}

    super_list = [
        {"firstname": "Abdel", "lastname":"Awesome"},
        {"firstname": "Karol", "lastname":"Pretty"},
        {"firstname": "Sofia", "lastname":"Beauty"},
        {"firstname": "Danny", "lastname":"Lovely"},
        {"firstname": "Mafe", "lastname":"Sweet"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)
    
    for i in range(len(super_list)):
        print(super_list[i])
    
    list_test = [] #list first 10 number ^{2}

    for i in range(1, 101): #First 100 numbers (1-100)
        x = i*i
        list_test.append(x)
    
    print(list_test)

if __name__ == '__main__': #Entry Point
    run()