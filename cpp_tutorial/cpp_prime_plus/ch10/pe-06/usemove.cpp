#include "move.h"
#include <cassert>

int main()
{
	Move m1;
	assert(m1 == Move(0, 0));

	Move m2(1, 3);
	assert(m2 == Move(1, 3));

	Move m3 = m1.Add(m2);
	assert(m3 == Move(1, 3));

	m1.reset(5, 5);
	assert(m1 == Move(5, 5));

	m3 = m1.Add(m2);
	assert(m3 == Move(6, 8));

	return 0;
}