// strngbad.cpp -- StringBad 클래스의 메서드
#include <cstring>
#include "strngbad.h"

using std::cout;

// static 클래스 멤버를 초기화 한다
int StringBad::num_strings = 0;

// 클래스 메서드

// C 스타일의 문자열로부터 StringBad를 생성한다
StringBad::StringBad(const char* s)
{
	len = std::strlen(s);			// 문자열의 크기를 설정
	str = new char[len + 1];		// 기억 공간을 대입한다
	std::memcpy(str, s, len + 1);	// 포인터를 초기화 한다
	num_strings++;					// 생성된 객체 수를 카운트한다
	cout << num_strings << ": \"" << str
		<< "\" 객체 생성\n";		// 추적용 메시지
}

StringBad::StringBad()				// 디폴트 생성자
{
	len = 3;
	str = new char[len + 1];
	std::memcpy(str, "C++", len + 1);
	num_strings++;
	cout << num_strings << ": \"" << str
		<< "\" 디폴트 객체 생성\n";	// 추적용 메시지
}

StringBad::StringBad(const StringBad& other)
	: len(other.len)
{
	str = new char[len + 1];
	std::memcpy(str, other.str, len + 1);
	num_strings++;
	cout << "복사 생성자 호출\n";
}

StringBad::~StringBad()				// 꼭 필요한 파괴자
{
	cout << "\"" << str << "\" 객체 파괴, ";			// 추적용 메시지
	--num_strings;										// 필요하다
	cout << "남은 객체 수: " << num_strings << "\n";	// 추적용 메시지
	delete[] str;										// 필요하다
}

StringBad& StringBad::operator=(const StringBad& rhs)
{
	if (this == &rhs)
	{
		return *this;
	}

	delete[] str;

	len = rhs.len;
	str = new char[len + 1];
	std::memcpy(str, rhs.str, len + 1);

	cout << "대입 연산자 호출\n";

	return *this;
}

std::ostream& operator<<(std::ostream& os, const StringBad& st)
{
	os << st.str;
	return os;
}
