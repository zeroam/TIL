#include "02.h"
#include <iostream>

namespace num2
{
	void program()
	{
		using std::cout;
		const int ARR_SIZE = 10;

		int arr[ARR_SIZE];
		int size = get_arr(arr, ARR_SIZE);
		print_arr(arr, size);
		double mean = get_mean(arr, size);
		cout << "����� " << mean << "�Դϴ�.\n";
		cout << "���α׷��� �����մϴ�.\n";
	}

	int get_arr(int arr[], int size)
	{
		using std::cout;
		using std::cin;

		cout << "���� ���ھ �Է��Ͻÿ�\n";
		for (int i = 0; i < size; i++)
		{
			cout << "#" << i + 1 << ": ";
			cin >> arr[i];

			if (cin.fail())
				return i;
		}

		return size;
	}

	void print_arr(int arr[], int size)
	{
		using std::cout;

		cout << "���� ���ھ� ����\n";
		for (int i = 0; i < size; i++)
			cout << "#" << i + 1 << ":" << arr[i] << ", ";
		cout << "\n";

	}

	double get_mean(int arr[], int size)
	{
		double sum = 0;

		for (int i = 0; i < size; i++)
			sum += (double)arr[i];
		sum = sum / size;

		return sum;
	}
}