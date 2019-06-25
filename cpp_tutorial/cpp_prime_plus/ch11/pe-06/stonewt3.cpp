// stonewt.cpp
#include <iostream>
#include "stonewt3.h"

using std::cout;

Stonewt::Stonewt(double lbs, Mode mode)
	:mPounds(lbs)
	, mMode(mode)
{
	mStone = int(lbs) / Lbs_per_stn;
	mPds_left = int(lbs) % Lbs_per_stn + lbs - int(lbs);
}

Stonewt::Stonewt(int stn, double lbs, Mode mode)
	: mStone(stn)
	, mPds_left(lbs)
	, mMode(mode)
{
	mPounds = stn * Lbs_per_stn + lbs;
}

Stonewt::Stonewt()
	: Stonewt(0.0)
{
}

Stonewt::~Stonewt()
{
}

Stonewt Stonewt::operator+(const Stonewt& rhs)
{
	Stonewt sum;
	sum.mPounds = mPounds + rhs.mPounds;
	setStone(sum);

	return sum;
}

Stonewt Stonewt::operator-(const Stonewt& rhs)
{
	Stonewt diff;
	if (mPounds < rhs.mPounds)
	{
		cout << "결과 값이 음수 입니다.\n";
		return NULL;
	}

	diff.mPounds = mPounds - rhs.mPounds;
	setStone(diff);

	return diff;
}

Stonewt Stonewt::operator*(const Stonewt& rhs)
{
	Stonewt mul;
	mul.mPounds = mPounds * rhs.mPounds;
	setStone(mul);

	return mul;
}

Stonewt & Stonewt::operator=(const Stonewt & rhs)
{
	if (this == &rhs)
	{
		return *this;
	}

	mPounds = rhs.mPounds;
	setStone(*this);

	return *this;
}

bool Stonewt::operator==(const Stonewt& rhs) const
{
	return mPounds == rhs.mPounds && mStone == rhs.mStone
		&& mPds_left == rhs.mPds_left && mMode == rhs.mMode;
}

std::ostream& operator<<(std::ostream& os, Stonewt& rhs)
{
	switch (rhs.mMode)
	{
	case Stonewt::Mode::STONE:
		cout << rhs.mStone << "스톤, " << rhs.mPds_left << "파운드";
		break;
	case Stonewt::Mode::DB_POUNDS:
		cout << rhs.mPounds << "파운드";
		break;
	case Stonewt::Mode::INT_POUNDS:
		cout << static_cast<int>(rhs.mPounds) << "파운드";
		break;
	default:
		break;
	}

	return os;
}

void Stonewt::setStone(Stonewt& st)
{
	int intPounds = static_cast<int>(mPounds);
	st.mStone = intPounds / Lbs_per_stn;
	st.mPds_left = intPounds % Lbs_per_stn + mPounds - intPounds;
}