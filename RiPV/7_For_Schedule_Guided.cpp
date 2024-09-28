// Выводит время начала, время остановки, продолжительность и точность таймера.
#include <iostream>
#include <omp.h>
#include <IntSafe.h>

int main() {
    double start, stop, duration;
    const int N = 20000;
    int y[N];
    start = omp_get_wtime();

    #pragma omp parallel
    {
        #pragma omp for schedule (guided, 3)
        for (int i = 1; i < N; ++i) {
            y[i] = (i - 1) * (i + 1);
            #pragma omp critical
            std::cout << "Dynamic. ThreadNum= " << omp_get_thread_num()
                      << "  Iteration: " << i << "  y= " << y[i] << std::endl;
        }
    }
    stop = omp_get_wtime();
    duration = stop - start;
    std::cout << "Start time: " << start
              << " Stop time:" << stop
              << " Duration: " << duration
              << " Accuracy: " <<omp_get_wtick() << std::endl;
}
