// secref.cpp -- ���� ������ ���ǿ� ���
#include <iostream>
int main()
{
	using namespace std;
	int rats = 101;
	int& rodents = rats;		// rodents�� �����̴�

	cout << "rats = " << rats;
	cout << ", rodents = " << rodents << endl;

	cout << "rats�� �ּ� = " << &rats;
	cout << ", rodents�� �ּ� = " << &rodents << endl;

	int bunnies = 50;
	rodents = bunnies;		// ������ �ٲ� �� �ִ°�?
	cout << "bunnies = " << bunnies;
	cout << ", rats = " << rats;
	cout << ", rodents = " << rodents << endl;

	cout << "bunnies�� �ּ� = " << &bunnies;
	cout << ", rodents�� �ּ� = " << &rodents << endl;

	return 0;
}