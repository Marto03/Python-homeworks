from math import sqrt
class NumberZeroError(Exception):
    pass

#class FloatNumberError(Exception):
#    pass


#class WordError(Exception):
#    pass
while True:
    try:
        number = int(input("Input an integer number: "))
        if number == 0:
            raise NumberZeroError
        #if number == str:
        #    raise WordError
        #if number == float:
        #    raise FloatNumberError
        print(f"{sqrt(number):.2f}")
        break
    except ValueError:
        print("Invalid number, try again!")

    except NumberZeroError:
        print("Cant give a square root of 0!")

    #except FloatNumberError:
    #    print("Cant give a square root of float.")
    #except WordError:
    #    print("Words don't have square roots.")

    finally:
        print("Good Bye")

