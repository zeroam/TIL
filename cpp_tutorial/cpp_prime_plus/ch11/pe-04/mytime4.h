// mytime4.h -- �����带 ����ϴ� Time Ŭ����
#pragma once
#include <iostream>

class Time
{
public:
	Time();
	Time(int h, int m = 0);
	void AddMin(int m);
	void AddHr(int h);
	void Reset(int h = 0, int m = 0);

	friend Time operator+(const Time& lhs, const Time& rhs);
	friend Time operator-(const Time& lhs, const Time& rhs);
	friend Time operator*(const Time& lhs, double n);
	friend Time operator*(double m, const Time& t) { return t * m; }
	friend std::ostream& operator<<(std::ostream& os, const Time& t);

private:
	int hours;
	int minutes;
};
