// inline.cpp -- �ζ��� �Լ� ����ϱ�
#include <iostream>

// �ζ��� �Լ� ����
inline double square(double x) { return x * x; }

int main()
{
	using namespace std;
	double a, b;
	double c = 13.0;

	a = square(5.0);
	b = square(4.5 + 7.5);		// ���ĵ� ������ �� �ִ�.
	cout << "a = " << a << ", b = " << b << endl;
	cout << "c = " << c;
	cout << ", c�� ���� = " << square(c++) << endl;
	cout << "���� c = " << c << endl;

	return 0;
}