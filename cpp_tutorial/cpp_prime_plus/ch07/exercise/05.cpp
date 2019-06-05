#include "05.h"
#include <iostream>

namespace num5
{
	void program()
	{
		using namespace std;

		cout << "factorial(0): " << factorial(0) << endl;
		cout << "factorial(1): " << factorial(1) << endl;
		cout << "factorial(2): " << factorial(2) << endl;
		cout << "factorial(3): " << factorial(3) << endl;
		cout << "factorial(4): " << factorial(4) << endl;
		cout << "factorial(5): " << factorial(5) << endl;
		cout << "factorial(10): " << factorial(10) << endl;
	}

	size_t factorial(size_t n)
	{
		if (n < 2)
			return 1;

		return n * factorial(n - 1);
	}
}