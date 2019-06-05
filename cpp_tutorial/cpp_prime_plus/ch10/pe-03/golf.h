#pragma once

class Golf
{
public:
	Golf(): mHandicap(0) {};
	Golf(const char* name, int hc);
	int SetGolf();

	inline void Handicap(int hc);
	void ShowGolf();

private:
	enum { LEN = 40 };
	char mFullName[LEN];
	int mHandicap;
};

void Golf::Handicap(int hc)
{
	mHandicap = hc;
}