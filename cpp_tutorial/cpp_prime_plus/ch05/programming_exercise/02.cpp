#include "02.h"
#include <iostream>
#include <array>
const int ArSize = 101;

void num2::program()
{
	using namespace std;

	array<long double, ArSize> factorials;
	factorials[1] = factorials[2] = 1L;
	for (int i = 2; i < ArSize; i++)
		factorials[i] = i * factorials[i-1];
	for (int i = 0; i < ArSize; i++)
		cout << i << "! = " << factorials[i] << endl;
}
