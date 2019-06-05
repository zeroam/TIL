#pragma once

class Plorg
{
public:
	Plorg(const char* name = "Plorg", int CI = 50);

	inline void SetCI(int CI);
	void Show();

private:
	enum { MAX = 20 };
	char mName[MAX];
	int mCI;
};

void Plorg::SetCI(int CI)
{
	mCI = CI;
}