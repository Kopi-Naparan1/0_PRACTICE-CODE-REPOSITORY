

def exercise_1():
    test_1 = [i for i in range(1,21) if i % 2 == 0]
    print(test_1)


def exercise_2():
    words = ["hello", "world", "python"]
    test_2 = [len(word) for word in words]
    print(f'Total letters: {sum(test_2)}')


def exercise_3():
    test_3 = [f'odd {i}' if i % 2 == 1 else f'even {i}' for i in range(1,21)]
    print(test_3)


def exercise_4():
    test_4 = [i ** 2 for i in range(1, 20) if i % 3 == 0]
    print(test_4)


def exercise_5():
    # to get the len (it cancels len)
    test_5 = {len(word) for word in ["hi", "hello", "hi", "world"]}
    print(test_5)


def exercise_6():
    # to get the len (it cancels len)
    test_6 = {n ** 2: n for n in range(1, 6)}
    print(test_6)


def exercise_7():
    matrix = [[i * j for j in range(5)] for i in range(5)]
    print(matrix)

    flat = [item for row in matrix for item in row]
    print(flat)


def exercise_8():
    # 5x5 grid of zeroes
    grid = [[0 for _ in range(5)] for _ in range(5)]
    print("Zero Grid:")
    print(grid)

    # Multiplication table stretch
    table = [[i * j for i in range(1, 6)] for j in range(1, 6)]
    print("Multiplication Table:")
    print(table)


def exercise_9():
    test_7 = (i for i in range(100000) if i % 2 == 1)
    i = 1
    for num in test_7:
        if i < 1001:
            print(num)
            i += 1
        else:
            break


def exercise_10():
    test_8 = sum(i**2 for i in range(1001))
    print(f'Total sum: {test_8}')


def main():
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
    exercise_7()
    exercise_8()
    exercise_9()
    exercise_10()

if __name__ == "__main__":
    main()