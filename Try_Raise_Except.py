def run():
    # string[::-1] inversion del string
    #eval mirror words
    def palindrome(string):
        try:
            if len(string) == 0:
                #Levanta un error cuando esta condicion es cumplida
                raise ValueError("Not empty strings allow")
            return string == string[::-1]
        except ValueError as ve:
            print(ve)
            return False
        finally:
            print("Done")

    try:
        print(palindrome(""))
    except TypeError:
        print("Only Strings allow")


if __name__ == '__main__': #Entry Point
    run()