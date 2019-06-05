#include "02.h"
#include <iostream>

void num2::program()
{
	using namespace std;
	double arr[10];
	double num;
	int i;
	for (i = 0; i < 10; i++)
	{
		cout << "기부금 #" << i << ": ";
		cin >> num;
		if (cin.fail())
			break;
		arr[i] = num;
	}
	
	double mean = getMean(arr, i);
	int count = biggerThanMean(arr, i, mean);

	cout << "기부금들의 평균: " << mean
		<< ", 평균보다 큰 기부금의 갯수: " << count << endl;
}

double num2::getMean(double * arr, int size)
{
	double sum = 0;
	for (int i = 0; i < size; i++)
	{
		sum += arr[i];
	}
	return sum / size;
}

int num2::biggerThanMean(double * arr, int size, double mean)
{
	int count = 0;
	for (int i = 0; i < size; i++)
	{
		if (arr[i] > mean)
			count++;
	}
	return count;
}
