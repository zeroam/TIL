#include "plorg.h"
#include <iostream>

Plorg::Plorg(const char* name, int CI)
	: mCI(CI)
{
	memcpy(mName, name, MAX - 1);
	mName[MAX - 1] = '\0';
}

void Plorg::Show()
{
	std::cout << "ÀÌ¸§: " << mName
		<< ", CI: " << mCI << std::endl;
}