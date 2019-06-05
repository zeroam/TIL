#pragma once

namespace num10
{
	typedef double(*p_fun)(double, double);
	void program();

	double calculate(double x, double y, p_fun pf);
	double add(double x, double y);
	double sub(double x, double y);
	double mul(double x, double y);
}