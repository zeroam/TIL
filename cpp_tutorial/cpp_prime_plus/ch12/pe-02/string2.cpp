// string1.cpp
#include <cstring>
#include <cctype>
#include "string2.h"

// static 클래스 멤버 초기화
int String::numStrings = 0;

// static 메서드
size_t String::HowMany()
{
	return numStrings;
}

// 클래스 메서드
String::String(const char* str)
{
	mLen = strlen(str);
	mStr = new char[mLen + 1];
	memcpy(mStr, str, mLen + 1);
	numStrings++;
}

String::String()
	: String("")
{
}

String::String(const String& other)
{
	numStrings++;
	mLen = other.mLen;
	mStr = new char[mLen + 1];
	memcpy(mStr, other.mStr, mLen + 1);
}

String::~String()
{
	--numStrings;
	delete[] mStr;
}

void String::stringlow()
{
	for (size_t i = 0; i < mLen; i++)
	{
		mStr[i] = std::tolower(mStr[i]);
	}
}

void String::stringup()
{
	for (size_t i = 0; i < mLen; i++)
	{
		mStr[i] = std::toupper(mStr[i]);
	}
}

int String::has(const char ch) const
{
	int count = 0;
	for (size_t i = 0; i < mLen; i++)
	{
		if (mStr[i] == ch)
		{
			count++;
		}
	}

	return count;
}

// 오버로드 연산자 메서드
String& String::operator=(const String& rhs)
{
	if (this == &rhs)
	{
		return *this;
	}

	delete[] mStr;
	mLen = rhs.mLen;
	mStr = new char[mLen + 1];
	memcpy(mStr, rhs.mStr, mLen + 1);

	return *this;
}

String& String::operator=(const char* str)
{
	delete[] mStr;
	mLen = strlen(str);
	mStr = new char[mLen + 1];
	memcpy(mStr, str, mLen + 1);

	return *this;
}


char& String::operator[](int i)
{
	return mStr[i];
}

const char& String::operator[](int i) const
{
	return mStr[i];
}


// 오버로드 연산자 프렌드
String operator+(const String& lhs, const String& rhs)
{
	String result;
	result.mLen = lhs.mLen + rhs.mLen;

	delete[] result.mStr;
	result.mStr = new char[result.mLen + 1];

	
	memcpy(result.mStr, lhs.mStr, lhs.mLen + 1);
	char* ptr = result.mStr + lhs.mLen;
	for (size_t i = 0; i < rhs.mLen; i++)
	{
		*ptr = rhs.mStr[i];
		ptr++;
	}
	*ptr = '\0';

	return result;
}

bool operator<(const String& lhs, const String& rhs)
{
	size_t len = lhs.mLen > rhs.mLen ? lhs.mLen : rhs.mLen;
	return (std::strncmp(lhs.mStr, rhs.mStr, len + 1) < 0);
}

bool operator>(const String& lhs, const String& rhs)
{
	return rhs < lhs;
}

bool operator==(const String& lhs, const String& rhs)
{
	size_t len = lhs.mLen > rhs.mLen ? lhs.mLen : rhs.mLen;
	return (std::strncmp(lhs.mStr, rhs.mStr, len + 1) == 0);
}


// 간단한 문자열 출력
std::ostream& operator<<(std::ostream& os, const String& rhs)
{
	os << rhs.mStr;
	return os;
}

// 빠르고 지저분한 문자열 입력
std::istream& operator>>(std::istream& is, String& rhs)
{
	char temp[String::CINLIM];
	is.get(temp, String::CINLIM);
	if (is)
	{
		rhs = temp;	// 대입 연산자 호출
	}
	
	while (is && is.get() != '\n')
	{
		continue;
	}

	return is;
}
