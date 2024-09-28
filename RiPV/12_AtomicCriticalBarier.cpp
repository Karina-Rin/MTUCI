// Измеряет и выводит общее время выполнения и точность используемого таймера.
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
            //#pragma omp atomic
            value++;
            #pragma omp barrier
            //#pragma omp critical (cout)
            {
                std::cout << value++ << " ";
            }

        }
        cout << endl;
    }
    stop = omp_get_wtime();
    duration = stop - start;
    std::cout << "Start time: " << start
              << " Stop time:" << stop
              << " Duration: " << duration
              << " Accuracy: " <<omp_get_wtick() << std::endl;
}
