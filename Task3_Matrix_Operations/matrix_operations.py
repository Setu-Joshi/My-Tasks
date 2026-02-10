import numpy as np


def input_matrix(rows, cols):
    print(f"Enter elements row-wise ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    return np.array(matrix)


def matrix_addition(A, B):
    return A + B


def matrix_subtraction(A, B):
    return A - B


def matrix_multiplication(A, B):
    return np.dot(A, B)


def matrix_transpose(A):
    return A.T


def matrix_determinant(A):
    return np.linalg.det(A)


def main():
    print("=== Matrix Operations Tool ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")

    choice = int(input("Choose an operation (1-5): "))

    if choice in [1, 2, 3]:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        print("\nMatrix A:")
        A = input_matrix(rows, cols)

        print("\nMatrix B:")
        B = input_matrix(rows, cols)

        if choice == 1:
            result = matrix_addition(A, B)
            print("\nResult (A + B):\n", result)

        elif choice == 2:
            result = matrix_subtraction(A, B)
            print("\nResult (A - B):\n", result)

        elif choice == 3:
            result = matrix_multiplication(A, B)
            print("\nResult (A x B):\n", result)

    elif choice == 4:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        A = input_matrix(rows, cols)
        print("\nTranspose of Matrix:\n", matrix_transpose(A))

    elif choice == 5:
        size = int(input("Enter size of square matrix: "))
        A = input_matrix(size, size)
        print("\nDeterminant of Matrix:", matrix_determinant(A))

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
