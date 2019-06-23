#pragma once

class Cow
{
public:
	Cow();
	Cow(const char* nm, const char* ho, double weight);
	Cow(const Cow& other);
	~Cow();
	Cow& operator=(const Cow& rhs);
	void ShowCow() const;

private:
	char name[20];
	char* hobby;
	double weight;
};
