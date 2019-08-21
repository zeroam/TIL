// string2.h
#pragma once
#include <iostream>

class String
{
public:
	// 생성자와 기타 메서드
	String(const char* str);
	String();
	String(const String& other);
	~String();
	size_t length() const { return mLen; }
	void stringlow();
	void stringup();
	int has(const char ch) const;

	// 오버로딩 연산자 메서드
	String& operator=(const String& rhs);
	String& operator=(const char* str);
	char& operator[](int index);
	const char& operator[](int index) const;

	// 오버로딩 연산자 프렌드
	friend String operator+(const String& lhs, const String& rhs);
	friend bool operator<(const String& lhs, const String& rhs);
	friend bool operator>(const String& lhs, const String& rhs);
	friend bool operator==(const String& lhs, const String& rhs);
	friend std::ostream& operator<<(std::ostream& os, const String& rhs);
	friend std::istream& operator>>(std::istream& is, String& rhs);

	// static 함수
	static size_t HowMany();

private:
	char* mStr;						// 문자열을 지시하는 포인터
	size_t mLen;						// 문자열 길이
	static int numStrings;			// 객체의 수
	static const int CINLIM = 80;	// cin 입력 한계
};