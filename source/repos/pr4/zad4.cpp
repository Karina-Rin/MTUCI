// ����������� ���������� �������� � ������� VS �������� ��������� � �������������� ������� VC++�

// 4 ������ � ��� ���������� � ��� ������������� ��������
#include <iostream>
#include <cmath>
#define _USE_MATH_DEFINES
#include "math.h"
using namespace std;

void func4(void);  // ���������� (��������) ������� func4
double x, y, c;     // ���������� ����������

int main()
{
    setlocale(LC_ALL, "rus");
    cout << " ���� x= ";
    cin >> x;
    cout << endl << "���� y= ";
    cin >> y;
    func4(); // ����� �������
    cout << endl << "��� x = " << x << " � y = " << y << endl;
    cout << endl << "��������� c= " << c << endl;
    system("PAUSE");
    return 0;
}
// ����������� ������� func4
void func4()
{
    c = x * log10(fabs(x - 6)) - (sin(pow(x, 2)) / (y * pow(x, 3)));
}