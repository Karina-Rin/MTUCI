// Выводит время начала, время остановки, продолжительность выполнения и 
// точность таймера
#include <iostream>
#include <omp.h>
#include <IntSafe.h>

using std::cout;
using std::endl;

int main() {
    double start, stop, duration;
    start = omp_get_wtime();

    for (int i = 1; i <= 5; i++)
    {
        int value = 123;
        
        #pragma omp parallel
        {
            value++;
            // #pragma omp critical
            // {
                //std::cout << value++ << " ";
            //}
            std::cout << value++ << " ";
        }
        std::cout << std::endl;
    }

    stop = omp_get_wtime();
    duration = stop - start;

    std::cout << "Start time: " << start
              << " Stop time:" << stop
              << " Duration: " << duration
              << " Accuracy: " <<omp_get_wtick() << std::endl;
}
