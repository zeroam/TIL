#include "05.h"
#include <iostream>

void num5::program()
{
	using namespace std;
	cout << "�ҵ��� �Է��Ͻÿ� : ";

	double pay;
	double tax;
	cin >> pay;
	if (cin.fail() || pay < 0)
	{
		cout << "����� �� ���ڸ� �Է��ϼž� �մϴ�.\n���α׷��� �����մϴ�.";
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

	cout << "���ž� �� ������ " << tax << " Ʈ��Ʈ �Դϴ�.";

}
