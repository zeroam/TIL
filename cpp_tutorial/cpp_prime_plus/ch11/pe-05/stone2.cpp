#include "stonewt2.h"
#include <iostream>
#include <cassert>

int main()
{
	using namespace std;
	Stonewt temp;

	Stonewt stone1;
	cout << "stone1: " << stone1 << endl;
	assert(stone1 == Stonewt(0.0, Stonewt::Mode::STONE));

	Stonewt stone2(3.5);
	Stonewt stone3(12.7);
	temp = stone2 + stone3;
	cout << "stone2: " << stone2 << endl;
	cout << "stone3: " << stone3 << endl;
	cout << "stone2 + stone3: " << temp << endl;
	assert(temp == Stonewt(16.2, Stonewt::Mode::STONE));

	temp = stone2 - stone3;
	cout << "stone2 - stone3: " << temp << endl;
	assert(temp == NULL);

	temp = stone3 - stone2;
	cout << "stone3 - stone2: " << temp << endl;
	assert(temp == Stonewt(9.2, Stonewt::Mode::STONE));

	temp = stone2 * stone3;
	cout << "stone2 * stone3: " << temp << endl;

	temp.setMode(Stonewt::Mode::DB_POUNDS);
	cout << "temp: " << temp << endl;

	temp.setMode(Stonewt::Mode::INT_POUNDS);
	cout << "temp: " << temp << endl;

	return 0;
}