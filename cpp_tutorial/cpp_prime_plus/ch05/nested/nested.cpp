// nested.cpp -- ��ø ������ 2���� �迭
#include <iostream>
const int Cities = 5;
const int Years = 4;

int main()
{
	using namespace std;
	const char* cities[Cities] =				// 5���� ���ڿ��� �����ϴ� �������� �迭
	{
		"Seoul",
		"Jeju",
		"Busan",
		"Gangneung",
		"Daegu"
	};

	int maxtemps[Years][Cities] =				// 2���� �迭
	{
		{35, 32, 33, 36, 35},
		{33, 32, 34, 35, 31},
		{33, 34, 32, 35, 34},
		{36, 35, 34, 37, 35}
	};

	cout << "2009����� 2012������� ���� �ְ� �µ�\n\n";
	for (int city = 0; city < Cities; city++)
	{
		cout << cities[city] << ":\t";
		for (int year = 0; year < Years; year++)
			cout << maxtemps[year][city] << "\t";
		cout << endl;
	}

	return 0;
}