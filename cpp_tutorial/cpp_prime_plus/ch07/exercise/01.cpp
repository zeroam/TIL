#include "01.h"
#include <iostream>

void num1::program()
{
	using namespace std;

	double x;
	double y;
	double result;

	cout << "���� �� ���� �����ؼ� �Է��Ͻʽÿ�: ";
	while (cin >> x >> y)
	{
		if (x == 0 || y == 0)
			break;
		result = num1::get_mean(x, y);
		cout << "��ȭ����� " << result << "�Դϴ�\n";
		cout << "���� �� ���� �����ؼ� �Է��Ͻʽÿ�: ";
	}
	cout << "���α׷��� �����մϴ�.";
}

double num1::get_mean(double x, double y)
{
	return 2.0 * x * y / (x + y);
}