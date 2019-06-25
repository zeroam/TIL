// mytime4.cpp -- Time 클래스의 메서드 구현
#include "mytime4.h"

Time::Time()
	: Time(0, 0)
{
}

Time::Time(int h, int m)
	: hours(h)
	, minutes(m)
{
}

void Time::AddMin(int m)
{
	minutes += m;
	hours += minutes / 60;
	minutes %= 60;
}

void Time::AddHr(int h)
{
	hours += h;
}

void Time::Reset(int h, int m)
{
	hours = h;
	minutes = m;
}

Time operator+(const Time& lhs, const Time& rhs)
{
	Time sum;
	sum.minutes = lhs.minutes + rhs.minutes;
	sum.hours = lhs.hours + rhs.hours + sum.minutes / 60;
	sum.minutes %= 60;
	return sum;
}

Time operator-(const Time& lhs, const Time& rhs)
{
	Time diff;
	int tot1, tot2;
	tot1 = rhs.minutes + 60 * rhs.hours;
	tot2 = lhs.minutes + 60 * lhs.hours;
	diff.minutes = (tot2 - tot1) % 60;
	diff.hours = (tot2 - tot1) / 60;
	return diff;
}

Time operator*(const Time& lhs, double mult)
{
	Time result;
	long totalminutes = lhs.hours * mult * 60 + lhs.minutes * mult;
	result.hours = totalminutes / 60;
	result.minutes = totalminutes % 60;
	return result;
}

std::ostream& operator<<(std::ostream& os, const Time& t)
{
	os << t.hours << "시간, " << t.minutes << "분";
	return os;
}