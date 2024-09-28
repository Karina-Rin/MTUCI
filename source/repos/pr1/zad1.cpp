// «Разработка консольных проектов и решения VS 
//  линейной структуры с использованием функций VC++»
// 1 проект – функция func1 с входными параметрами и возвращаемым 
// значением вначале, а после нее программный код главной функции main
#include <iostream>
#include <cmath>
#define _USE_MATH_DEFINES
#include "math.h"
using namespace std;

// Определение функции func1
double func1(double x, double y)
{
    double c;     // Локальный объект
    c = x * log10(fabs(x - 6)) - (sin(pow(x, 2)) / (y * pow(x, 3)));
    return c;     // Возврат c в вызывающую функцию
}

int main()
{
    setlocale(LC_ALL, "rus");
    double x, y, c;
    cout << " Ввод x= ";
    cin >> x;
    cout << endl << "Ввод y= ";
    cin >> y;
    c = func1(x, y); // Вызов функции func1
    cout << endl << "При x = " << x << " и y = " << y << endl;
    cout << endl << "результат c= " << c << endl;
    system("PAUSE");
    return 0;
}
