#include "07.h"
#include <iostream>

namespace num7
{
	const int Max = 5;

	void program()
	{
		using namespace std;
		double properties[Max];

		double* end = fill_array(properties, Max);
		show_array(properties, end);
		if (end - properties > 0)
		{
			cout << "재평가율을 입력하십시오: ";
			double factor;
			while (!(cin >> factor))
			{
				cin.clear();
				while (cin.get() != '\n')
					continue;
				cout << "잘못 입력했습니다, 수치를 입력하세요: ";
			}
			ravalue(factor, properties, end);
			show_array(properties, end);
		}
		cout << "프로그램을 종료합니다.\n";
		cin.get();
		cin.get();
	}

	double* fill_array(double ar[], int limit)
	{
		double temp;
		int i;
		for (i = 0; i < limit; i++)
		{
			using std::cout;
			using std::cin;

			cout << (i + 1) << "번 부동산의 가격: $";
			cin >> temp;
			if (!cin)
			{
				cin.clear();
				while (cin.get() != '\n')
					continue;
				cout << "입력 불량; 입력 과정을 끝내겠습니다.\n";
				break;
			}
			else if (temp < 0)
				break;
			ar[i] = temp;
		}
		return &ar[i];
	}

	void show_array(const double ar[], const double end[])
	{
		int count = 1;
		for (const double* ptr = ar; ptr != end; ptr++)
		{
			std::cout << count << "번 부동산: $";
			std::cout << *ptr << std::endl;
			count++;
		}
	}

	void ravalue(double r, double ar[], const double end[])
	{
		for (double* ptr = ar; ptr != end; ptr++)
			*ptr *= r;
	}
}