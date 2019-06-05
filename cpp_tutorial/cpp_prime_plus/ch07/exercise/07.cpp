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
			cout << "�������� �Է��Ͻʽÿ�: ";
			double factor;
			while (!(cin >> factor))
			{
				cin.clear();
				while (cin.get() != '\n')
					continue;
				cout << "�߸� �Է��߽��ϴ�, ��ġ�� �Է��ϼ���: ";
			}
			ravalue(factor, properties, end);
			show_array(properties, end);
		}
		cout << "���α׷��� �����մϴ�.\n";
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

			cout << (i + 1) << "�� �ε����� ����: $";
			cin >> temp;
			if (!cin)
			{
				cin.clear();
				while (cin.get() != '\n')
					continue;
				cout << "�Է� �ҷ�; �Է� ������ �����ڽ��ϴ�.\n";
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
			std::cout << count << "�� �ε���: $";
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