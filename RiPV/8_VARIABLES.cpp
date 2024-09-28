// Программа измеряет и выводит время выполнения каждого потока
#include <iostream>
#include <omp.h>
#include <IntSafe.h>

int main() {
    double start, stop, duration;
    start = omp_get_wtime();
    int i, j, a =10, b = 20, c = 30, d=40;
    i = omp_get_num_threads();
    j = omp_get_thread_num();
    std::cout <<"Begin.Treads:Total = " <<i <<" MyNum= " <<j<<std::endl;
    std::cout <<"a = " <<a <<" b = " <<b <<" c = " <<c <<" d = " <<d<<std::endl;
    
    #pragma omp parallel sections private (i, j) firstprivate (a) shared (b) num_threads (3)
    {
        int d=100;
        i = omp_get_num_threads();
        j = omp_get_thread_num();
        a = a + j; d = d + j;

        # pragma omp critical
        {
            b = j;
            c = j;
            std::cout <<"Parallel section.Treads:Total = " <<i<<" MyNum= " <<j <<std::endl;
            std::cout <<" a= " <<a <<" b= " <<b <<" c= " <<c <<" d= "<<d <<std::endl;
        }
    }

    std::cout << "Final. Treads:Total = " <<i <<" MyNum = " <<j<< std::endl;
    std::cout <<" a= " <<a <<" b= " <<b <<" c= " <<c <<" d= " <<d << std::endl;

    stop = omp_get_wtime();
    duration = stop - start;
    std::cout << "Start time: " << start
              << " Stop time:" << stop
              << " Duration: " << duration
              << " Accuracy: " <<omp_get_wtick() << std::endl;
}