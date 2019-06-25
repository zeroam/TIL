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

	cout << "최대 원소: " << max << endl;
	cout << "최소 원소: " << min << endl;
	cout << "11스톤보다 크거나 같은 원소의 갯수: " << num << endl;

	return 0;
}