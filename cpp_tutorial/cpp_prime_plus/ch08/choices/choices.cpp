// choices.cpp -- ���ø� ����
#include <iostream>

template <class T>				// #1
T lesser(T a, T b)
{
	return a < b ? a : b;
}

int lesser(int a, int b)		// #2
{
	a = a < 0 ? -a : a;
	b = b < 0 ? -b : b;
	return a < b ? a : b;
}

int main()
{
	using namespace std;
	int m = 20;
	int n = -30;
	double x = 15.5;
	double y = 25.9;

	cout << lesser(m, n) << endl;		// #2�� ����Ѵ�
	cout << lesser(x, y) << endl;		// double�� �Բ� #1�� ����Ѵ�
	cout << lesser<>(m, n) << endl;		// int�� �Բ� #1�� ����Ѵ�
	cout << lesser<int>(x, y) << endl;	// int�� �Բ� #1�� ����Ѵ�

	return 0;
}