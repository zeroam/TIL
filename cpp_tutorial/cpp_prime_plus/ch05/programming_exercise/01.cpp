#include "01.h"
#include <iostream>

void num1::program()
{
	using namespace std;

	int num1, num2;

	cout << "�ΰ��� ������ �Է��Ͻÿ�: ";
	cin >> num1;
	cin >> num2;

	int sum = 0;
	for (int i = num1; i <= num2; i++)
	{
		sum += i;
	}

	cout << "�������� ��: " << sum;
}