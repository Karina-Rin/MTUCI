// Выводит локальные суммы из каждого потока и общую сумму элементов массива,
// а также информацию о времени.
#include <iostream>
#include <omp.h>
#include <IntSafe.h>

int main() {
    double start, stop, duration;
    start = omp_get_wtime();
    const int N = 100;
    long int s = 0;
    int a[N];

    for (int i = 0; i < N; i++) {
        a[i] = i;
    }
    
    #pragma omp parallel reduction(+: s)
    {
        #pragma omp for
        for (int i = 0; i < N; i++)
        s += a[i];
        #pragma omp critical
        {
            std::cout << " ThreadNum = " << omp_get_thread_num()<< " Local Sum = " << s << std::endl;
        }
    }

    std::cout << " Total Sum = " << s << std::endl;
    stop = omp_get_wtime();
    duration = stop - start;
    std::cout << "Start time: " << start
              << " Stop time:" << stop
              << " Duration: " << duration
              << " Accuracy: " <<omp_get_wtick() << std::endl;
}
