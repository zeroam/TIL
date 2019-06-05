#pragma once

class Move
{
public:
	Move(double a = 0, double b = 0) : mX(a), mY(b) {}

	void ShowMove() const;
	Move Add(const Move& m) const;

	inline void reset(double a = 0, double b = 0) { mX = a; mY = b; }

	inline bool operator==(const Move& rhs) { return mX == rhs.mX && mY == rhs.mY; }

private:
	double mX;
	double mY;
};
