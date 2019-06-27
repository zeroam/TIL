// dma.cpp -- DMA Ŭ���� �޼����
#include <cstring>
#include "dma.h"

// baseDMA �޼����
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
	os << "��ǥ: " << rs.label << std::endl;
	os << "���: " << rs.rating << std::endl;
	return os;
}

// lacksDMA �޼����
lacksDMA::lacksDMA(const char* c, const char* l, int r)
	: baseDMA(l, r)
{
	memcpy(color, c, strlen(c) + 1);
}

std::ostream& operator<<(std::ostream& os, const lacksDMA& ls)
{
	os << static_cast<const baseDMA&>(ls);
	os << "����: " << ls.color << std::endl;
	return os;
}

// hasDMA �޼����
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
	: baseDMA(hs)		// ���� Ŭ���� ���� �����ڸ� ȣ���Ѵ�
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
	baseDMA::operator=(hs);		// ���� Ŭ���� �κ��� �����Ѵ�
	delete[] style;				// ���ο� ��Ÿ���� �غ��϶�
	style = new char[strlen(hs.style) + 1];
	memcpy(style, hs.style, strlen(hs.style) + 1);

	return *this;
}

std::ostream& operator<<(std::ostream& os, const hasDMA& hs)
{
	os << static_cast<const baseDMA&>(hs);
	os << "��Ÿ��: " << hs.style << std::endl;
	return os;
}
