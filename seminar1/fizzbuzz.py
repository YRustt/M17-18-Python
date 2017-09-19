

if __name__ == '__main__':
    fizz, buzz, fizzbuzz = map(int, input('Enter fizz, bizz and fizzbuzz with a space: ').split())

    for i in range(1, 50, 2):
        if i % 15 == 0:
            print(fizzbuzz, end=' ')
        elif i % 5 == 0:
            print(buzz, end=' ')
        elif i % 3 == 0:
            print(fizz, end=' ')
        print(i, end=' ')
