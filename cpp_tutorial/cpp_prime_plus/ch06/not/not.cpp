// not.cpp -- not ������
#include <iostream>
#include <climits>
bool is_int(double);
int main()
{
	using namespace std;
	double num;

	cout << "���� ���� �ϳ� �Է��Ͻʽÿ�: ";
	cin >> num;
	while (!is_int(num))	// num�� int���� ������ �� ���� ���̸� ���
	{
		cout << "int���� ������ �� ���� ���Դϴ�. �ٽ� �Է��Ͻʽÿ�: ";
		cin >> num;
	}
	int val = int(num);		// �������� ��ȯ
	cout << "����� �Է��� ������ " << val << "�Դϴ�.\n";
	return 0;
}

bool is_int(double x)
{
	if (x <= INT_MAX && x >= INT_MIN)	// climits�� �ִ� �� ���
		return true;
	else
		return false;
}