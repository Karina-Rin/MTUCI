// ����������� ���������� �������� � ������� VS 
//  �������� ��������� � �������������� ������� VC++�

// 3-� ������ � ��� ������������� ��������, �� ������� �� �������� ��������
#include <iostream>
#include <cmath>
#define _USE_MATH_DEFINES
#include "math.h"
using namespace std;
// ���������� (��������) ������� func3
void func3(double, double, double&);
int main()
{
    setlocale(LC_ALL, "rus");
    double x, y, c;
    cout << " ���� x= ";
    cin >> x;
    cout << endl << "���� y= ";
    cin >> y;
    func3(x, y, c);  // ����� ������� func3
    cout << endl << "��� x = " << x << " � y = " << y << endl;
    cout << endl << "��������� c= " << c << endl;
    system("PAUSE");
    return 0;
}
// ����������� ������� func3
void func3(double x, double y, double& c)
{
    c = x * log10(fabs(x - 6)) - (sin(pow(x, 2)) / (y * pow(x, 3)));
}
