def sum_rows(arr):
    row_sums = []
    for row in arr:
        row_sum = sum(row)
        row_sums.append(row_sum)
    return row_sums


if __name__ == "__main__":
 
    two_dim_array = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]


    row_sums = sum_rows(two_dim_array)

    print("Суми рядків двовимірного масиву:")
    print(row_sums)
