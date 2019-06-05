#pragma once

namespace num7
{
	void program();

	struct debts
	{
		char name[50];
		double amount;
	};

	template <typename T>
	T SumArray(T arr[], int n);

	template <typename T>
	T SumArray(T* arr[], int n);
}
