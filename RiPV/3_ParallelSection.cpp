// Программа выводит время начала, номера нитей для каждого раздела,
// время окончания и продолжительность выполнения.
#include <iostream>
#include <omp.h>
#include <IntSafe.h>
#include <windows.h> // Include this header for GetTickCount

int main() {
    const int MAXSIZE = 1000;
    int i;
    DWORD t1, t2;
    float a[MAXSIZE], b[MAXSIZE];
    int k, m;
    t1 = GetTickCount();
    std::cout<< " t1 = " << t1 << std::endl;

    #pragma omp parallel sections private (i) shared (a,b)
    {
        #pragma omp section
        {
            for (i = 1; i < MAXSIZE; ++i) {
                a[i] = i*0.1;
            }
            m = omp_get_thread_num();
            std::cout << "My number is " << m<< std::endl;
        }

        #pragma omp section
        {
            k = omp_get_thread_num();
            std::cout << "My number is " << k << std::endl;
            for (i = 1; i < MAXSIZE; ++i){
                b[i] = (float)i*0.2;
            }
        }
    }

    t2 = GetTickCount();
    std::cout<< " t2 = " << t2 << std::endl;
    std::cout << "Duration = " << t2 - t1 << std::endl;
}
