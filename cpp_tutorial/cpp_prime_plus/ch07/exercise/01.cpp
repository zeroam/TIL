#include "01.h"
#include <iostream>

void num1::program()
{
	using namespace std;

	double x;
	double y;
	double result;

	cout << "숫자 두 개를 연속해서 입력하십시오: ";
	while (cin >> x >> y)
	{
		if (x == 0 || y == 0)
			break;
		result = num1::get_mean(x, y);
		cout << "조화평균은 " << result << "입니다\n";
		cout << "숫자 두 개를 연속해서 입력하십시오: ";
	}
	cout << "프로그램을 종료합니다.";
}

double num1::get_mean(double x, double y)
{
	return 2.0 * x * y / (x + y);
}