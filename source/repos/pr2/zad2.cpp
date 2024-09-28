#include <iostream>
#include <cmath>
using namespace std;

// Описание функции (прототип)
//double func2(double, double);
int main()
{
    setlocale(LC_ALL, "rus");
    double x, y, c;
    cout << " Ввод x= ";
    cin >> x;
    cout << endl << "Ввод y= ";
    cin >> y;
    c = func2(x, y); // Вызов функции func1
    cout << endl << "При x = " << x << " и y = " << y << endl;
    cout << endl << "результат c= " << c << endl;
    system("PAUSE");
    return 0;
}

// Определение функции func1
double func2(double x, double y)
{
    double c;     // Локальный объект
    c = x * log10(fabs(x - 6)) - (sin(pow(x, 2)) / (y * pow(x, 3)));
    return c;     // Возврат c в вызывающую функцию
}

