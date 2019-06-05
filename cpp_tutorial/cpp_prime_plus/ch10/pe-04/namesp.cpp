#include "namesp.h"
#include <iostream>

namespace SALES
{
	Sales::Sales()
	{
		for (int i = 0; i < QUARTERS; i++)
		{
			std::cout << i + 1 << "분기 판매액 : ";
			std::cin >> mSales[i];
		}

		mMax = mSales[0];
		mMin = mSales[0];
		mAverage = mSales[0];

		for (int i = 1; i < QUARTERS; i++)
		{
			if (mMax < mSales[i])
			{
				mMax = mSales[i];
			}
			if (mMin > mSales[i])
			{
				mMin = mSales[i];
			}
			mAverage += mSales[i];
		}
		mAverage /= QUARTERS;
	}

	Sales::Sales(const double ar[], int n)
	{
		int num = QUARTERS < n ? QUARTERS : n;
		memset(mSales, 0, sizeof(double) * QUARTERS);

		if (num == 0)
		{
			return;
		}

		memcpy(mSales, ar, sizeof(double) * num);

		mMax = ar[0];
		mMin = ar[0];
		mAverage = ar[0];

		for (int i = 1; i < num; i++)
		{
			if (mMax < ar[i])
			{
				mMax = ar[i];
			}
			if (mMin > ar[i])
			{
				mMin = ar[i];
			}
			mAverage += ar[i];
		}
		mAverage /= num;
	}

	void Sales::ShowSales() const
	{
		std::cout << "판매 결과:\n";
		std::cout << "  최대 : $" << mMax << std::endl;
		std::cout << "  최소 : $" << mMin << std::endl;
		std::cout << "  평균 : $" << mAverage << std::endl;
	}
}