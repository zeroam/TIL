#include "05.h"
#include <iostream>

void num5::program()
{
	using namespace std;
	cout << "소득을 입력하시오 : ";

	double pay;
	double tax;
	cin >> pay;
	if (cin.fail() || pay < 0)
	{
		cout << "제대로 된 숫자를 입력하셔야 합니다.\n프로그램을 종료합니다.";
		return;
	}
		
	if (pay <= 5000)
		tax = 0;
	else if (pay <= 15000)
	{
		pay -= 5000;
		tax = pay * 0.1;
	}
	else if (pay <= 35000)
	{
		pay -= 15000;
		tax = pay * 0.15 + 10000 * 0.1;
	}
	else
	{
		pay -= 35000;
		tax = pay * 0.2 + 20000 * 0.15 + 10000 * 0.1;
	}

	cout << "내셔야 할 세금은 " << tax << " 트바트 입니다.";

}
