// caio silas de araujo amaro
// 21.1.4111


/*
    caso base
    T(0) = 0
    T(1) = 1

    caso recursivo
    T(n) = 23 + x + T(n/2)
    
    T(n/2) = 23 + x + T(n/4)
    T(n/4) = 23 + x + T(n/8)
    T(n) = 23*k + x*k + T(n/2^k)
    n/2^k = 1
    n = 2^k
    k = log n
    T(n) = 23 log n + log n + 1


    PIOR CASO
    x = 1
    T(n) = 24 log n + 1
    T(n) = $\Theta(log n)$.

    MELHOR CASO
    x = 0
    23 log n + 1 => T(n) = $\Theta(log n)$.

    CASO MEDIO
    0 * 1/2 + 1 * 1/2 = x = 1/2
    23 log n + 1/2 log n + 1
    23,5 log n + 1 => T(n) = O(log n)

*/

#include <stdlib.h>
#include <stdio.h>
#include <math.h>

void multiply(int F[2][2], int M[2][2]) {
    int x = F[0][0] * M[0][0] + F[0][1] * M[1][0];
    int y = F[0][0] * M[0][1] + F[0][1] * M[1][1];
    int z = F[1][0] * M[0][0] + F[1][1] * M[1][0];
    int w = F[1][0] * M[0][1] + F[1][1] * M[1][1];

    F[0][0] = x;
    F[0][1] = y;
    F[1][0] = z;
    F[1][1] = w;
}

void power(int F[2][2], int n) {
    if (n <= 1)
        return;

    int M[2][2] = {{1, 1}, {1, 0}};

    power(F, n / 2);
    multiply(F, F);

    if (n % 2 != 0)
        multiply(F, M);
}

int fibonacci(int n) {
    if (n <= 0)
        return 0;

    int F[2][2] = {{1, 1}, {1, 0}};
    power(F, n - 1);

    return F[0][0];
}

int main() {
    int n;

    printf("Digite qual o valor de Fibonacci você deseja calcular: ");
    scanf("%d", &n);

    int result = fibonacci(n);
    printf("O %dº número de Fibonacci é: %d\n", n, result);

    return 0;
}