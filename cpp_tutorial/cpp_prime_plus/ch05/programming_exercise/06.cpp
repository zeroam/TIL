#include "06.h"
#include <iostream>
const int Months = 12;

void num6::program()
{
	using namespace std;
	/*
	const char* months[Months] =
	{
		"1��", "2��", "3��", "4��", "5��", "6��",
		"7��", "8��", "9��", "10��", "11��", "12��"
	};
	*/
	char months[Months][5] =
	{
		"1��", "2��", "3��", "4��", "5��", "6��",
		"7��", "8��", "9��", "10��", "11��", "12��"
	};
	int sales[3][Months];

	int total = 0;
	for (int i = 0; i < 3; i++)
	{
		for (int j = 0; j < Months; j++)
		{
			cout << months[j] << "�� ������� �Է��Ͻʽÿ�: ";
			cin >> sales[i][j];
			total += sales[i][j];
		}
		cout << i + 1 << "�� ���� �� �Ǹž�: " << total << "��" << endl;
	}

}
