// Каждый поток выводит свой номер потока, текущий индекс итерации и 
// соответствующие значения.
#include <iostream>
#include <omp.h>
#include <IntSafe.h>

int main() {
    const int N = 20;
    int x[N], y[N];

    #pragma omp parallel
    {
        #pragma omp for
        for (int i = 1; i < N; ++i) {
            y[i] = (i - 1) * (i + 1);
        }
        #pragma omp for
        for (int i = 1; i < N; ++i) {
            x[i] = (y[i - 1] + y[i]) / 2;
        }
        
        #pragma omp for
        for (int i = 1; i < N; ++i) {
            #pragma omp critical
            std::cout << "ThreadNum=" << omp_get_thread_num()
                      << " Iteration: " << i
                      << " y=" << y[i]
                      << " x=" << x[i] << std::endl;
        }
    }
}
