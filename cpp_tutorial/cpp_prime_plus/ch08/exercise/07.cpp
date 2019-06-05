#include "07.h"
#include <iostream>

namespace num7
{
	void program()
	{
		using namespace std;
		int things[6] = { 13, 31, 103, 301, 310, 310 };
		debts mr_E[3] =
		{
			{"Ima Wolfe", 2400.0},
			{"Ura Foxe", 1300.0},
			{"Iby Stout", 1800.0}
		};
		double* pd[3];

		// �����͵��� �迭 mr_E�� �ִ� ����ü���� amount ����� �����Ѵ�
		for (int i = 0; i < 3; i++)
		{
			pd[i] = &mr_E[i].amount;
		}

		cout << "Mr. E�� ��� ����: " << SumArray(things, 6) << endl;
		cout << "Mr. E�� ä�� ����: " << SumArray(pd, 3) << endl;
	}

	template <typename T>
	T SumArray(T arr[], int n)
	{
		T sum = 0;
		for (int i = 0; i < n; i++)
		{
			sum += arr[i];
		}
		return sum;
	}

	template <typename T>
	T SumArray(T* arr[], int n)
	{
		T sum = 0;
		for (int i = 0; i < n; i++)
		{
			sum += *arr[i];
		}
		return sum;
	}
}