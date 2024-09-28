// «Разработка консольных проектов и решения VS линейной структуры с использованием функций VC++»

// 4 проект – без параметров и без возвращаемого значения
#include <iostream>
#include <cmath>
#define _USE_MATH_DEFINES
#include "math.h"
using namespace std;

void func4(void);  // Объявление (прототип) функции func4
double x, y, c;     // Глобальные переменные

int main()
{
    setlocale(LC_ALL, "rus");
    cout << " Ввод x= ";
    cin >> x;
    cout << endl << "Ввод y= ";
    cin >> y;
    func4(); // Вызов функции
    cout << endl << "При x = " << x << " и y = " << y << endl;
    cout << endl << "результат c= " << c << endl;
    system("PAUSE");
    return 0;
}
// Определение функции func4
void func4()
{
    c = x * log10(fabs(x - 6)) - (sin(pow(x, 2)) / (y * pow(x, 3)));
}