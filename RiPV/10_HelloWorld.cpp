// Вывод Hello world в консоль
#include <iostream>
#include <omp.h>

int main() {
    #pragma omp parallel
    {
        std::cout << "Hello  World ";
    }
    std::cout << std::endl;
}
