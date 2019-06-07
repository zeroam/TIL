#include "03.h"
#include <iostream>

void num3::program()
{
	using namespace std;
	int num;
	
	cout << "숫자를 하나 입력하시오: ";
	cin >> num;
	int sum = num;
	while (num != 0)
	{
		cout << "숫자를 하나 입력하시오: ";
		cin >> num;
		sum += num;
	}
	cout << "총합은 " << sum << "입니다.";
}