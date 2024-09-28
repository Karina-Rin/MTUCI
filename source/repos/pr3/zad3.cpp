// «Разработка консольных проектов и решения VS 
//  линейной структуры с использованием функций VC++»

// 3-й проект – без возвращаемого значения, со ссылкой на выходной параметр
#include <iostream>
#include <cmath>
#define _USE_MATH_DEFINES
#include "math.h"
using namespace std;
// Объявление (прототип) функции func3
void func3(double, double, double&);
int main()
{
    setlocale(LC_ALL, "rus");
    double x, y, c;
    cout << " Ввод x= ";
    cin >> x;
    cout << endl << "Ввод y= ";
    cin >> y;
    func3(x, y, c);  // Вызов функции func3
    cout << endl << "При x = " << x << " и y = " << y << endl;
    cout << endl << "результат c= " << c << endl;
    system("PAUSE");
    return 0;
}
// Определение функции func3
void func3(double x, double y, double& c)
{
    c = x * log10(fabs(x - 6)) - (sin(pow(x, 2)) / (y * pow(x, 3)));
}
