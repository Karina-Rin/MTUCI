#include <iostream>
#include <cmath>
using namespace std;

double func2(double, double);
int main()
{
    setlocale(LC_ALL, "rus");
    double x, y, c;
    cout << " ���� x= ";
    cin >> x;
    cout << endl << "���� y= ";
    cin >> y;
    c = func2(x, y); // ����� ������� func1
    cout << endl << "��� x = " << x << " � y = " << y << endl;
    cout << endl << "��������� c= " << c << endl;
    system("PAUSE");
    return 0;
}