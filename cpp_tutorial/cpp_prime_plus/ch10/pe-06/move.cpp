#include "move.h"
#include <iostream>

void Move::ShowMove() const
{
	std::cout << "x: " << mX << ", y: " << mY << std::endl;
}

Move Move::Add(const Move& m) const
{
	Move result;
	result.mX = mX + m.mX;
	result.mY = mY + m.mY;
	return result;
}