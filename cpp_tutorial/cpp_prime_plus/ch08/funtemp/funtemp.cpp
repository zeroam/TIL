// funtemp.cpp -- �Լ� ���ø� ����ϱ�
#include <iostream>
// �Լ� ���ø� ����
template <typename Any>
void Swap(Any& a, Any& b);

int main()
{
	using namespace std;
	int i = 10;
	int j = 20;
	cout << "i, j = " << i << ", " << j << ".\n";
	cout << "�����Ϸ��� ������ int�� ��ȯ�⸦ ����ϸ�\n";
	Swap(i, j);			// void Swap(int&, int&)�� �����Ѵ�
	cout << "���� i, j = " << i << ", " << j << ".\n";

	double x = 24.5;
	double y = 81.7;
	cout << "x, y = " << x << ", " << y << ".\n";
	cout << "�����Ϸ��� ������ double�� ��ȯ�⸦ ����ϸ�\n";
	Swap(x, y);			// void Swap(double&, double&)�� �����Ѵ�
	cout << "���� x, y = " << x << ", " << y << ".\n";

	return 0;
}

// �Լ� ���ø� ����
template <typename Any>
void Swap(Any& a, Any& b)
{
	Any temp;
	temp = a;
	a = b;
	b = temp;
}