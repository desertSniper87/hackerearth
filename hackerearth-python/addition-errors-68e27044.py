if __name__ == '__main__':
    n_test_cases = int(input())
    for _ in range(n_test_cases):
        a = input()[::-1]
        b = input()[::-1]

        ret = ['0']
        for x, y in zip(a, b):
            x, y = int(x), int(y)
            ret.insert(0, str(((x+y)//10)))
        print(int("".join(x for x in ret)))
