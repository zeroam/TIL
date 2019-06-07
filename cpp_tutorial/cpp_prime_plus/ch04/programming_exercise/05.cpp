#include "05.h"
#include <iostream>

void exercise::number5()
{
	using namespace std;
	struct CandyBar
	{
		char name[20];
		float weight;
		int cal;
	};

	CandyBar snack = { "Mocha Munch", 2.3, 350 };

	cout << "½º³¼ name: " << snack.name
		<< ", weight: " << snack.weight
		<< ", cal: " << snack.cal << endl;
}