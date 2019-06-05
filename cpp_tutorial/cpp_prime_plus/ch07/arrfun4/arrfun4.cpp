// arrfun4.cpp -- �迭 ������ ����ϴ� �Լ�
#include <iostream>
const int ArSize = 8;
int sum_arr(const int* begin, const int* end);
int main()
{
	using namespace std;
	int cookies[ArSize] = { 1, 2, 4, 8, 16, 32, 64, 128 };

	int sum = sum_arr(cookies, cookies + ArSize);
	cout << "���� ���� �� �հ�: " << sum << endl;
	sum = sum_arr(cookies, cookies + 3);		// ó�� 3���� ����
	cout << "ó�� �� ����� ���� " << sum << "���� �Ծ����ϴ�.\n";
	sum = sum_arr(cookies + 4, cookies + 8);	// ������ 4���� ����
	cout << "������ �� ����� ���� " << sum << "���� �Ծ����ϴ�.\n";
	return 0;
}

// ���� �迭�� �հ踦 �����Ѵ�
int sum_arr(const int* begin, const int* end)
{
	const int* pt;
	int total = 0;

	for (pt = begin; pt != end; pt++)
		total = total + *pt;
	return total;
}