#include <iostream>

#ifndef MATRIX_H
#define MATRIX_H

// Function to compute the dot product between two 1D arrays of numbers
int dot(int a[], int b[], int length) {
    int result = 0;
    for (int i = 0; i < length; ++i) {
        result += a[i] * b[i];
    }
    return result;
}

// Function to compute the cross product between two 1D arrays of length 3
void cross(int a[], int b[], int c[], int length = 3) {
    if (length == 3) {
        c[0] = a[1] * b[2] - a[2] * b[1];
        c[1] = a[2] * b[0] - a[0] * b[2];
        c[2] = a[0] * b[1] - a[1] * b[0];
    }
}

// Function to compute the prefix sum of a 1D array
void prefix_sum(int A[], int S[], int size) {
    S[0] = A[0];
    for (int i = 1; i < size; ++i) {
        S[i] = S[i - 1] + A[i];
    }
}

// Function to compute the diagonal of a square matrix (size 2 or 3)
void diagonal(int matrix[][3], int diagonal[], int size) {
    for (int i = 0; i < size; ++i) {
        diagonal[i] = matrix[i][i];
    }
}

// Function to check if a matrix is symmetric (supports different sizes)
template <size_t rows, size_t cols>
bool symmetric(int (&matrix)[rows][cols]) {
    if (rows != cols) {
        return false;
    }
    for (size_t i = 0; i < rows; ++i) {
        for (size_t j = 0; j < cols; ++j) {
            if (matrix[i][j] != matrix[j][i]) {
                return false;
            }
        }
    }
    return true;
}

// Function to multiply two matrices element-wise (Hadamard product)
void multiply(int A[][3], int B[][3], int C[][3], int r, int c) {
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            C[i][j] = A[i][j] * B[i][j];
        }
    }
}

#endif // MATRIX_H

int main() {
    // Example usage for dot product
    int a2[] = {5, -8};
    int b2[] = {1, 2};
    std::cout << dot(a2, b2, 2) << "\n";

    int a3[] = {1, 2, 3};
    int b3[] = {4, 5, 6};
    std::cout << dot(a3, b3, 3) << "\n";

    int a4[] = {0, 3, -7, 1};
    int b4[] = {2, 3, 1, 3};
    std::cout << dot(a4, b4, 4) << "\n";

    int a5[] = {0, 3, -7, 1, 3};
    int b5[] = {9, 5, 2, 1, 6};
    std::cout << dot(a5, b5, 5) << "\n";

    // Example usage for cross product
    int a[] = {1, 2, 3};
    int b[] = {4, 5, 6};
    int c[3];
    cross(a, b, c);
    for (int i = 0; i < 3; ++i) {
        std::cout << c[i] << (i < 2 ? " " : "");
    }
    std::cout << "\n";

    int a_cross[] = {-1, 2, 5};
    int b_cross[] = {7, -3, 1};
    cross(a_cross, b_cross, c);
    for (int i = 0; i < 3; ++i) {
        std::cout << c[i] << (i < 2 ? " " : "");
    }
    std::cout << "\n";

    int a_cross2[] = {0, -1, 2};
    int b_cross2[] = {1, -5, 3};
    cross(a_cross2, b_cross2, c);
    for (int i = 0; i < 3; ++i) {
        std::cout << c[i] << (i < 2 ? " " : "");
    }
    std::cout << "\n";

    // Example usage for prefix sum
    const int size = 7;
    int A[] = {0, 1, 2, 3, 4, 5, 6};
    int S[size];
    prefix_sum(A, S, size);
    for (int i = 0; i < size; ++i) {
        std::cout << S[i] << (i < size - 1 ? " " : "");
    }
    std::cout << "\n";

    const int size2 = 6;
    int A2[] = {0, 10, 20, 30, 40, 50};
    int S2[size2];
    prefix_sum(A2, S2, size2);
    for (int i = 0; i < size2; ++i) {
        std::cout << S2[i] << (i < size2 - 1 ? " " : "");
    }
    std::cout << "\n";

    int A3[] = {0, -10, 10, 20, -20, 100};
    int S3[size2];
    prefix_sum(A3, S3, size2);
    for (int i = 0; i < size2; ++i) {
        std::cout << S3[i] << (i < size2 - 1 ? " " : "");
    }
    std::cout << "\n";

    // Example usage for diagonal
    const int size3 = 3;
    int m3[][size3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int d3[size3];
    diagonal(m3, d3, size3);
    for (int i = 0; i < size3; ++i) {
        std::cout << d3[i] << (i < size3 - 1 ? " " : "");
    }
    std::cout << "\n";

    // Example usage for symmetry check
    int m1[][size3] = {{3, 5, 9}, {5, 7, 1}, {9, 1, 5}};
    std::cout << symmetric(m1) << "\n";

    int m2[][size3] = {{3, 5, 10}, {5, 0, 6}, {10, 7, 1}};
    std::cout << symmetric(m2) << "\n";

    const int size4 = 2;
    int m3_sym[][size4] = {{0, 0}, {0, 0}};
    std::cout << symmetric(m3_sym) << "\n";

    int m4_sym[][size4] = {{0, 0}, {1, 0}};
    std::cout << symmetric(m4_sym) << "\n";

    // Example usage for matrix multiplication
    int A2_mult[][size3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int B2_mult[][size3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int C_mult[size3][size3];
    multiply(A2_mult, B2_mult, C_mult, size3, size3);
    for (int i = 0; i < size3; ++i) {
        for (int j = 0; j < size3; ++j) {
            std::cout << C_mult[i][j] << (j < size3 - 1 ? " " : "");
        }
        std::cout << "\n";
    }

    return 0;
}

