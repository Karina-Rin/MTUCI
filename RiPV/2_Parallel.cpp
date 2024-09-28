// Выводит информацию о том, сколько потоков используется и их 
// соответствующие идентификаторы во время выполнения.
#include <iostream>
#include <omp.h>

int main() {
    int i,j;
    i=omp_get_num_threads();
    j=omp_get_thread_num();
    std::cout <<"Secuent region. OMP_NUM_THREADS = " << i << " TREAD_NUM = " << j << std::endl;

    #pragma omp parallel private (i, j)
    {
        i=omp_get_num_threads();
        j=omp_get_thread_num();
        std::cout << "Parallel region 1. OMP_NUM_THREADS = " << i << " TREAD_NUM = " << j << std::endl;
    }

    #pragma omp parallel private (i, j) num_threads (6)
    {
        i=omp_get_num_threads();
        j=omp_get_thread_num();
        std::cout << "Parallel region 2. OMP_NUM_THREADS = " << i << " TREAD_NUM = " << j << std::endl;
    }
}
