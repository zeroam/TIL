#pragma once
#include <array>

namespace num8
{
	const int Seasons = 4;
	struct Exp
	{
		double expenses[Seasons];
	};

	void program1();
	void program2();

	void fill(std::array<double, Seasons>* pa);
	void fill(Exp* pa);
	void show(std::array<double, Seasons> da);
	void show(Exp da);
}
