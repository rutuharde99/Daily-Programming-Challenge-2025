def find_missing_number(arr, n):
    xor_all = 0
    xor_arr = 0

    # XOR of all numbers from 1 to n
    for i in range(1, n + 1):
        xor_all ^= i

    # XOR of all elements in the array
    for num in arr:
        xor_arr ^= num

    # Missing number
    return xor_all ^ xor_arr


if __name__ == "__main__":
    arr = [1, 3, 4, 5]  # Example: numbers from 1 to 5
    n = 5
    print("Missing number:", find_missing_number(arr, n))
