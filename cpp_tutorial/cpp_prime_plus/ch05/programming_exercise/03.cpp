#include "03.h"
#include <iostream>

void num3::program()
{
	using namespace std;
	int num;
	
	cout << "���ڸ� �ϳ� �Է��Ͻÿ�: ";
	cin >> num;
	int sum = num;
	while (num != 0)
	{
		cout << "���ڸ� �ϳ� �Է��Ͻÿ�: ";
		cin >> num;
		sum += num;
	}
	cout << "������ " << sum << "�Դϴ�.";
}