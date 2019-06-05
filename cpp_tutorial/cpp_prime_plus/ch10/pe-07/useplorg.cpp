#include "plorg.h"

int main()
{
	Plorg p1;
	p1.Show();

	Plorg p2("hello", 30);
	p2.Show();

	p1.SetCI(10);
	p1.Show();

	return 0;
}