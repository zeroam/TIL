#include "05.h"
#include <iostream>

namespace num5
{
	void program()
	{
		int arr1[] = { 32, 23, 53, 22, 12 };
		double arr2[] = { 10.5, 21.2, 13.5, 11.1, 19.2 };

		int max1 = max5(arr1);
		double max2 = max5(arr2);

		std::cout << "int형 max값: " << max1 << std::endl;
		std::cout << "double형 max값: " << max2 << std::endl;
	}

	template <typename T>
	T max5(const T arr[])
	{
		T max = arr[0];

		for (int i = 1; i < 5; i++)
		{
			if (max < arr[i])
			{
				max = arr[i];
			}
		}
		return max;
	}
}