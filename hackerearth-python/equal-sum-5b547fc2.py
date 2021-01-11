from collections import Counter

def main(total_len, sbarr_len, array):
    if total_len == sbarr_len:
        return True

    n_arrays = total_len // sbarr_len

    occurance = Counter(array)

    if len(occurance) > sbarr_len:
        return False
    for number in occurance:
        if occurance[number] % n_arrays != 0:
            return False;

    return True




n_test_cases = int(input())
for _ in range(n_test_cases):
    total_len, sbarr_len = map(int, input().split())
    array = list(map(int, input().split()))
    result = main(total_len, sbarr_len, array)
    
    if result:
        print("YES")
    else:
        print("NO")
