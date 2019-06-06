#include "06.h"
#include <iostream>
const int Months = 12;

void num6::program()
{
	using namespace std;
	/*
	const char* months[Months] =
	{
		"1월", "2월", "3월", "4월", "5월", "6월",
		"7월", "8월", "9월", "10월", "11월", "12월"
	};
	*/
	char months[Months][5] =
	{
		"1월", "2월", "3월", "4월", "5월", "6월",
		"7월", "8월", "9월", "10월", "11월", "12월"
	};
	int sales[3][Months];

	int total = 0;
	for (int i = 0; i < 3; i++)
	{
		for (int j = 0; j < Months; j++)
		{
			cout << months[j] << "의 매출액을 입력하십시오: ";
			cin >> sales[i][j];
			total += sales[i][j];
		}
		cout << i + 1 << "년 누적 총 판매액: " << total << "원" << endl;
	}

}
