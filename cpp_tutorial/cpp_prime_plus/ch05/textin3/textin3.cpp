// textin3.cpp -- 파일 끝까지 문자 읽기
#include <iostream>
int main()
{
	using namespace std;
	char ch;
	int count = 0;
	cin.get(ch);					// 문자 하나를 읽는다
	while (cin.fail() == false)		// EOF인지 검사한다
	{
		cout << ch;					// 문자를 에코한다
		++count;
		cin.get(ch);				// 다음 문자를 읽는다
	}
	cout << count << " 문자를 읽었습니다.\n";

	return 0;
}