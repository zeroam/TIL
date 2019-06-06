#include "05.h"
#include <iostream>
const int Months = 12;

void num5::program()
{
	using namespace std;

	const char* months[Months] =
	{
		"1월", "2월", "3월", "4월", "5월", "6월", 
		"7월", "8월", "9월", "10월", "11월", "12월"
	};
	int sales[Months];

	int total = 0;
	for (int i = 0; i < Months; i++)
	{
		cout << months[i] << "의 매출액을 입력하십시오: ";
		cin >> sales[i];
		total += sales[i];
	}

	cout << "연간 총 판매액: " << total << "원";
}
