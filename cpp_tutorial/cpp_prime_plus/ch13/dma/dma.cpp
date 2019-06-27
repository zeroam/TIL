// dma.cpp -- DMA 클래스 메서드들
#include <cstring>
#include "dma.h"

// baseDMA 메서드들
baseDMA::baseDMA(const char* l, int r)
{
	label = new char[strlen(l) + 1];
	memcpy(label, l, strlen(l) + 1);
	rating = r;
}

baseDMA::baseDMA(const baseDMA& rs)
{
	label = new char[strlen(rs.label) + 1];
	memcpy(label, rs.label, strlen(rs.label) + 1);
	rating = rs.rating;
}

baseDMA::~baseDMA()
{
	delete[] label;
}

baseDMA& baseDMA::operator=(const baseDMA& rs)
{
	if (this == &rs)
	{
		return *this;
	}
	delete[] label;

	label = new char[strlen(rs.label) + 1];
	memcpy(label, rs.label, strlen(rs.label) + 1);
	rating = rs.rating;

	return *this;
}

std::ostream& operator<<(std::ostream& os, const baseDMA& rs)
{
	os << "상표: " << rs.label << std::endl;
	os << "등급: " << rs.rating << std::endl;
	return os;
}

// lacksDMA 메서드들
lacksDMA::lacksDMA(const char* c, const char* l, int r)
	: baseDMA(l, r)
{
	memcpy(color, c, strlen(c) + 1);
}

std::ostream& operator<<(std::ostream& os, const lacksDMA& ls)
{
	os << static_cast<const baseDMA&>(ls);
	os << "색상: " << ls.color << std::endl;
	return os;
}

// hasDMA 메서드들
hasDMA::hasDMA(const char* s, const char* l, int r)
	: baseDMA(l, r)
{
	style = new char[strlen(s) + 1];
	memcpy(style, s, strlen(s) + 1);
}

hasDMA::hasDMA(const char* s, const baseDMA& rs)
	: baseDMA(rs)
{
	style = new char[strlen(s) + 1];
	memcpy(style, s, strlen(s) + 1);
}

hasDMA::hasDMA(const hasDMA& hs)
	: baseDMA(hs)		// 기초 클래스 복사 생성자를 호출한다
{
	style = new char[strlen(hs.style) + 1];
	memcpy(style, hs.style, strlen(hs.style) + 1);
}

hasDMA::~hasDMA()
{
	delete[] style;
}

hasDMA& hasDMA::operator=(const hasDMA& hs)
{
	if (this == &hs)
	{
		return *this;
	}
	baseDMA::operator=(hs);		// 기초 클래스 부분을 복사한다
	delete[] style;				// 새로운 스타일을 준비하라
	style = new char[strlen(hs.style) + 1];
	memcpy(style, hs.style, strlen(hs.style) + 1);

	return *this;
}

std::ostream& operator<<(std::ostream& os, const hasDMA& hs)
{
	os << static_cast<const baseDMA&>(hs);
	os << "스타일: " << hs.style << std::endl;
	return os;
}
