import numpy as np


def main():
    # Task 1: Init np matrix
    print("Task 1:")
    matrix = np.random.randint(0, 10, (4, 9))
    print(matrix, end='\n\n')

    # Task 2: array indicies
    print("Task 2:")
    print(matrix[2, 6], end='\n\n')

    # Task 3: even indicies only
    print("Task 3:")
    print(matrix[2][1::2], end='\n\n')

    #Task 4: reversed last column
    print("Task 4:")
    print(np.flip(matrix[:, -1]), end='\n\n')

    #Task 5: reshape matrix
    print("Task 5:")
    print(matrix := matrix.reshape((6, 6)), end='\n\n')

    # Task 6: power every array element
    print("Task 6:")
    print(matrix := np.power(matrix, 2), end='\n\n')

    # Task 7: main diag min
    print("Task 7:")
    print(matrix.diagonal().min(), end="\n\n")

    # Task 8: max of penultimate column
    print("Task 8:")
    print(matrix[:, -2].max(), end="\n\n")

    # Task 9: is non-decreasing sequence
    print("Task 9:")
    print(f"Flatten array diff: {(matrix_flatten_diff := np.diff(matrix.flatten()))}")
    print(f"Is non decreasing? {np.greater_equal(matrix_flatten_diff, 0).all()}", end="\n\n")

    # Task 10: prod of non-zero elements on ignoring diag
    print("Task 10:")
    print(np.prod(ign_diag := np.fliplr(matrix).diagonal(), where = ign_diag != 0), end="\n\n")

if __name__ == "__main__":
    main()
