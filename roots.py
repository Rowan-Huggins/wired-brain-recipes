def sqrt(x):
    """computing Sqaure Root"""
    guess = x
    i = 0
    while guess * guess !=x and i <20:
        guess = (guess +x/guess)/2.0
        i+=1
    return guess
def main():
    print(sqrt(9))
    print(sqrt(2))
    try:
        print(sqrt(-1))
    except ZeroDivisionError:
            print('cannot compute 0 division')


    print('program execution continues')

if __name__ == '__main__':
    main()
