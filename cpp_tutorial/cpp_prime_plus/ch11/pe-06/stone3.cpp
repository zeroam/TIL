#include "stonewt3.h"
#include <iostream>
#include <cassert>

int main()
{
	using namespace std;
	Stonewt stArr[6] =
	{
		Stonewt(11, 3.2),
		Stonewt(12, 4.5),
		Stonewt(30.4),
	};

	for (int i = 3; i < 6; i++)
	{
		stArr[i] = Stonewt(i * 20);
	}

	Stonewt max = stArr[0];
	Stonewt min = stArr[0];
	Stonewt compare(11, 0);
	int num = 0;

	for (int i = 0; i < 6; i++)
	{
		if (max < stArr[i])
		{
			max = stArr[i];
		}

		if (min > stArr[i])
		{
			min = stArr[i];
		}

		if (stArr[i] >= compare)
		{
			num++;
		}
	}

	cout << "�ִ� ����: " << max << endl;
	cout << "�ּ� ����: " << min << endl;
	cout << "11���溸�� ũ�ų� ���� ������ ����: " << num << endl;

	return 0;
}