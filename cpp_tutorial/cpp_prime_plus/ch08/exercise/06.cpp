#include "06.h"
#include <iostream>

namespace num6
{
	void program()
	{
		int arr1[] = { 5, 2, 1, 8, 11, 10 };
		double arr2[] = { 2.5, 3.1, 1.2, 8.9 };
		const char* strArr[] = { "Hello", "Bye", "God Bless you", "Good", "Nice" };

		int max1 = maxn(arr1, 6);
		double max2 = maxn(arr2, 4);
		const char* max3 = maxn(strArr, 5);

		std::cout << "int형 max값: " << max1 << std::endl;
		std::cout << "double형 max값: " << max2 << std::endl;
		std::cout << "const char*형 max값: " << max3 << std::endl;
	}

	template <typename T>
	T maxn(T arr[], int size)
	{
		T max = arr[0];
		for (int i = 1; i < size; i++)
		{
			if (max < arr[i])
			{
				max = arr[i];
			}
		}
		return max;
	}

	template<> const char* maxn<const char*>(const char* parr[], int size)
	{
		int* length = new int[size];
		for (int i = 0; i < size; i++)
		{
			length[i] = 0;
			while (*(parr[i] + length[i]))
			{
				length[i]++;
			}
		}

		const char* pmax = parr[0];
		int maxLength = length[0];

		for (int i = 1; i < size; i++)
		{
			if (maxLength < length[i])
			{
				maxLength = length[i];
				pmax = parr[i];
			}
		}
		return pmax;
	}
}