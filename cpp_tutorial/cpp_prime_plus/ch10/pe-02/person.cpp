#include "person.h"
#include <iostream>

Person::Person(const std::string& ln, const char* fn)
{
	lname = ln;
	memcpy(fname, fn, LIMIT);
	fname[LIMIT - 1] = '\0';
}

void Person::Show() const
{
	std::cout << fname << " " << lname << std::endl;
}

void Person::FormalShow() const
{
	std::cout << lname << ", " << fname << std::endl;
}