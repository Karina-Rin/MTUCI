#include <iostream>
#include <cmath>

using namespace std;

int main() {
    setlocale(LC_ALL, "rus");
    double x, y, c;
    int k, l, m, n;

    cout << "Введите х= ";
    cin >> x;
    cout << endl << "Введите y= ";
    cin >> y;
    // Вычисление выражения
    c = x * log10(fabs(x - 6)) - (sin(pow(x, 2)) / (y * pow(x, 3)));
    // Преобразования в целые числа
    k = c; // неявное
    l = int(c); // явное
    m = ceil(c);
    n = floor(c);

    // Вывод результатов
    cout << endl << "Вещественное с= " << c;
    cout << endl << "Целая часть результат (неявно) k= " << k;
    cout << endl << "Целая часть результат (явное преобразование) l= " << l;
    cout << endl << "Округление в большую сторону m= " << m;
    cout << endl << "Округление в меньшую сторону n= " << n<<endl;
    cout << endl << "Значение префиксного инкремента ++k= " <<++k;
    cout << endl << "Значение постфиксного инкремента l++= " << l++;
    cout << endl << "Значение k после приращения = " <<k;
    cout << endl << "Значение l после приращения = " << l<<endl<<endl;

    system("PAUSE");

    return 0;
}