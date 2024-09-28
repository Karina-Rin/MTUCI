// Выводит время начала, время окончания, продолжительность, точность таймера 
// и результат суммирования программы
#include <iostream>
#include <omp.h>

int main() {
    double start, stop, duration, s=1;
    const long int N = 500;
    start = omp_get_wtime();

    #pragma omp parallel reduction( + : s)
    {
        for (long int i = 1; i <= N; i++)
            s = s + i;
    }
    stop = omp_get_wtime();
    duration = stop - start;

    std::cout << "Start time: " << start
              << " Stop time:" << stop
              << " Duration: " << duration
              << " Accuracy: " <<omp_get_wtick() << std::endl;
    std::cout << " Result=" << s << std::endl;
}
