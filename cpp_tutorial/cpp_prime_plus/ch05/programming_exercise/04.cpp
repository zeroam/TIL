#include "04.h"
#include <iostream>

void num4::program()
{
	using namespace std;

	double customerA = 100000;
	double customerB = 100000;

	double moneyA = customerA * 0.1;
	double moneyB = customerB * 0.05;

	int year = 1;
	customerA += moneyA;
	customerB += moneyB;
	while (customerB < customerA)
	{
		year += 1;
		moneyB = customerB * 0.05;
		customerA += moneyA;
		customerB += moneyB;
	}

	cout << year << "�� ���" << endl;
	cout << "A�� ���ڰ�ġ: " << customerA << endl;
	cout << "B�� ���ڰ�ġ: " << customerB << endl;
}
