#include "05.h"
#include <iostream>
const int Months = 12;

void num5::program()
{
	using namespace std;

	const char* months[Months] =
	{
		"1��", "2��", "3��", "4��", "5��", "6��", 
		"7��", "8��", "9��", "10��", "11��", "12��"
	};
	int sales[Months];

	int total = 0;
	for (int i = 0; i < Months; i++)
	{
		cout << months[i] << "�� ������� �Է��Ͻʽÿ�: ";
		cin >> sales[i];
		total += sales[i];
	}

	cout << "���� �� �Ǹž�: " << total << "��";
}
