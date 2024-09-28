// Dыводит результаты каждой итерации, показывая, как различные потоки
// участвуют в вычислениях. Критический раздел гарантирует, что вывод
// остается удобочитаемым и организованным.
#include <iostream>
#include <omp.h>
#include <IntSafe.h> 

int main() {
    const int N = 20;
    int x[N+2], y[N+2];
    x[0] = 1;
    x[N + 1] = 1;
    y[0] = 0;
    y[N + 1] = 0;

    #pragma omp parallel
    {
        #pragma omp for
        for (int i = 1; i < N; ++i) {
            y[i] = (i - 1) * (i + 1);
            x[i] = (y[i - 1] + y[i]) / 2;

            #pragma omp critical
            {
                std::cout << "ThreadNum=" << omp_get_thread_num()
                          << " Iteration: " << i
                          << " x=" << x[i]
                          << " y=" << y[i] << "\n";
            }
        }
    }
} 
