// stonewt2.h
#pragma once
#include <iostream>

class Stonewt
{
public:
	enum Mode { STONE, INT_POUNDS, DB_POUNDS };

	Stonewt(double lbs, Mode mode = STONE);
	Stonewt(int stn, double lbs, Mode mode = STONE);
	Stonewt();
	~Stonewt();

	void setMode(Mode mode) { mMode = mode; }

	Stonewt operator+(const Stonewt& rhs);
	Stonewt operator-(const Stonewt& rhs);
	Stonewt operator*(const Stonewt& rhs);
	Stonewt& operator=(const Stonewt& rhs);
	bool operator==(const Stonewt& rhs) const;

	friend std::ostream& operator<<(std::ostream& os, Stonewt& rhs);

private:
	enum {Lbs_per_stn = 14};
	Mode mMode;
	int mStone;
	double mPds_left;
	double mPounds;

	void setStone(Stonewt& wt);
};
