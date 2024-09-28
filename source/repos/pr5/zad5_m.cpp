#include <iostream>
#include <cmath>
using namespace std;

double func2(double, double);
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