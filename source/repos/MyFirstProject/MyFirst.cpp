#include <iostream>
#include <cmath>

using namespace std;

int main() {
    setlocale(LC_ALL, "rus");
    double x, y, c;
    int k, l, m, n;

    cout << "������� �= ";
    cin >> x;
    cout << endl << "������� y= ";
    cin >> y;
    // ���������� ���������
    c = x * log10(fabs(x - 6)) - (sin(pow(x, 2)) / (y * pow(x, 3)));
    // �������������� � ����� �����
    k = c; // �������
    l = int(c); // �����
    m = ceil(c);
    n = floor(c);

    // ����� �����������
    cout << endl << "������������ �= " << c;
    cout << endl << "����� ����� ��������� (������) k= " << k;
    cout << endl << "����� ����� ��������� (����� ��������������) l= " << l;
    cout << endl << "���������� � ������� ������� m= " << m;
    cout << endl << "���������� � ������� ������� n= " << n<<endl;
    cout << endl << "�������� ����������� ���������� ++k= " <<++k;
    cout << endl << "�������� ������������ ���������� l++= " << l++;
    cout << endl << "�������� k ����� ���������� = " <<k;
    cout << endl << "�������� l ����� ���������� = " << l<<endl<<endl;

    system("PAUSE");

    return 0;
}