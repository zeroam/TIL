#include "sales.h"
#include <cstring>
#include <iostream>

namespace SALES
{
	void setSales(Sales& s, const double ar[], int n)
	{
		int num = QUARTERS < n ? QUARTERS : n;
		memset(s.sales, 0, sizeof(double) * QUARTERS);
		
		if (num == 0)
		{
			return;
		}

		memcpy(s.sales, ar, sizeof(double) * num);

		s.max = ar[0];
		s.min = ar[0];
		s.average = ar[0];

		for (int i = 1; i < num; i++)
		{
			if (s.max < ar[i])
			{
				s.max = ar[i];
			}
			if (s.min > ar[i])
			{
				s.min = ar[i];
			}
			s.average += ar[i];
		}
		s.average /= num;
	}

	void setSales(Sales& s)
	{
		for (int i = 0; i < QUARTERS; i++)
		{
			std::cout << i + 1 << "�б� �Ǹž� : ";
			std::cin >> s.sales[i];
		}

		s.max = s.sales[0];
		s.min = s.sales[0];
		s.average = s.sales[0];

		for (int i = 1; i < QUARTERS; i++)
		{
			if (s.max < s.sales[i])
			{
				s.max = s.sales[i];
			}
			if (s.min > s.sales[i])
			{
				s.min = s.sales[i];
			}
			s.average += s.sales[i];
		}
		s.average /= QUARTERS;
	}

	void showSales(const Sales& s)
	{
		std::cout << "�Ǹ� ���:\n";
		std::cout << "  �ִ� : $" << s.max << std::endl;
		std::cout << "  �ּ� : $" << s.min << std::endl;
		std::cout << "  ��� : $" << s.average << std::endl;
	}
}