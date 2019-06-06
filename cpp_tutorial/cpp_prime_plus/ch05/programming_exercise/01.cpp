#include "01.h"
#include <iostream>

void num1::program()
{
	using namespace std;

	int num1, num2;

	cout << "두개의 정수를 입력하시오: ";
	cin >> num1;
	cin >> num2;

	int sum = 0;
	for (int i = num1; i <= num2; i++)
	{
		sum += i;
	}

	cout << "정수들의 합: " << sum;
}