# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    max_num = float('-inf')
    second_max_num = float('-inf')
    for i in range(len(numbers)):
        if numbers[i] > max_num:
            second_max_num = max_num
            max_num = numbers[i]
            max_index = i

    for j in range(len(numbers)):
        if numbers[j] > second_max_num and j != max_index:  # first and second-largest number may have the same value, but must not have the same index. If they have the same index, then largest and second-largest numbers are same.
            second_max_num = numbers[j]

    # print(max_num, second_max_num)
    return max_num * second_max_num

if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
