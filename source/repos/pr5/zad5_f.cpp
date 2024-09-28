#include <iostream>
#include <cmath>
using namespace std;

// Определение функции func1
double func2(double x, double y)
{
    double c;     // Локальный объект
    c = x * log10(fabs(x - 6)) - (sin(pow(x, 2)) / (y * pow(x, 3)));
    return c;     // Возврат c в вызывающую функцию
}