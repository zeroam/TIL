#include "06.h"
#include <iostream>

namespace num6
{
	void program()
	{
		double arr[10];
		int size = Fill_array(arr, 10);
		Show_array(arr, size);
		Reverse_array(arr, size);
		Show_array(arr, size);
	}

	int Fill_array(double arr[], int size)
	{
		char ch;
		std::cout << "배열에 저장할 숫자를 입력하시오\n";

		for (int i = 0; i < size; i++)
		{
			std::cout << "#" << i + 1 << ": ";
			std::cin >> arr[i];

			if (std::cin.fail())
			{
				std::cin.clear();
				while ((ch = std::cin.get()) != '\n');
				return i;
			}
		}

		return size;
	}

	void Show_array(double arr[], int size)
	{
		for (int i = 0; i < size; i++)
		{
			std::cout << arr[i] << ", ";
		}
		std::cout << "\n";
	}

	void Reverse_array(double arr[], int size)
	{
		double* start = arr;
		double* end = arr + size - 1;
		double temp;
		while (start < end)
		{
			temp = *start;
			*start = *end;
			*end = temp;

			start++;
			end--;
		}
	}
}