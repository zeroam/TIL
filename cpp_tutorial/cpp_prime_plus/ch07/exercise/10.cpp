#include "10.h"
#include <iostream>

namespace num10
{
	void program()
	{
		p_fun pa[3] = { add, sub, mul };
		
		double result;
		for (int i = 0; i < 3; i++)
		{
			result = calculate(2.5, 10.4, pa[i]);
			std::cout << "°á°ú : " << result << std::endl;
		}
			
	}

	double calculate(double x, double y, p_fun pf)
	{
		return pf(x, y);
	}

	double add(double x, double y)
	{
		return x + y;
	}

	double sub(double x, double y)
	{
		return x - y;
	}

	double mul(double x, double y)
	{
		if (y == 0)
			return -1;

		return x / y;
	}
}