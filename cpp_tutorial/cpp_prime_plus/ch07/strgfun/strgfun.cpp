// strgfun.cpp -- 문자열 매개변수와 함수
#include <iostream>
unsigned int c_in_str(const char* str, char ch);
int main()
{
	using namespace std;
	char mmm[15] = "minimum";		// 배열에 들어 있는 문자열

	const char *wail = "ululate";			// wail은 문자열을 지시한다

	unsigned int ms = c_in_str(mmm, 'm');
	unsigned int us = c_in_str(wail, 'u');
	cout << mmm << "에는 m이 " << ms << "개 들어있습니다.\n";
	cout << wail << "에는 u가 " << us << "개 들어있습니다.\n";
	return 0;
}

// 이 함수는 str 문자열에 들어 있는
// ch 문자의 개수를 카운트 한다
unsigned int c_in_str(const char* str, char ch)
{
	int count = 0;

	while (*str)
	{
		if (*str == ch)
			count++;
		str++;
	}
	return count;
}