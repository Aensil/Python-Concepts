def run():
    #Temporary Funtion Lambda
    # string[::-1] inversion del string
    #eval mirror words
    palindrome = lambda string: string == string[::-1]

    print(palindrome('ana'))




if __name__ == '__main__': #Entry Point
    run()