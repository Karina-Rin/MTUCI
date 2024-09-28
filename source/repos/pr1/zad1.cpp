// ����������� ���������� �������� � ������� VS 
//  �������� ��������� � �������������� ������� VC++�
// 1 ������ � ������� func1 � �������� ����������� � ������������ 
// ��������� �������, � ����� ��� ����������� ��� ������� ������� main
#include <iostream>
#include <cmath>
#define _USE_MATH_DEFINES
#include "math.h"
using namespace std;

// ����������� ������� func1
double func1(double x, double y)
{
    double c;     // ��������� ������
    c = x * log10(fabs(x - 6)) - (sin(pow(x, 2)) / (y * pow(x, 3)));
    return c;     // ������� c � ���������� �������
}

int main()
{
    setlocale(LC_ALL, "rus");
    double x, y, c;
    cout << " ���� x= ";
    cin >> x;
    cout << endl << "���� y= ";
    cin >> y;
    c = func1(x, y); // ����� ������� func1
    cout << endl << "��� x = " << x << " � y = " << y << endl;
    cout << endl << "��������� c= " << c << endl;
    system("PAUSE");
    return 0;
}
