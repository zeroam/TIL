#include "string2.h"

using namespace std;

int main()
{
	String s1(" and I am a C++ student.");
	String s2 = "영문 이름을 입력하십시오: ";
	String s3;
	cout << s2;					// 오버로딩된 << 연산자
	cin >> s3;					// 오버로딩된 >> 연산자
	s2 = "My name is " + s3;	// 오버로딩된 =, + 연산자
	cout << s2 << ".\n";
	s2 = s2 + s1;
	s2.stringup();				// 문자열을 대문자로 변환한다
	cout << "다음 문자열에는\n" << s2 << "\n문자 'A'가 "
		<< s2.has('A') << "개 들어 있습니다.\n";
	s1 = "red";					// String(const char*)와
								// String& operator(const String&)을 사용한다
	String rgb[3] = { String(s1), String("green"), String("blue") };

	cout << "빛의 삼원색의 이름을 하나만 입력하십시오: ";
	String ans;
	bool success = false;
	while (cin >> ans)
	{
		ans.stringlow();		// 문자열을 소문자로 변환한다
		for (int i = 0; i < 3; i++)
		{
			if (ans == rgb[i])
			{
				cout << "맞았습니다!\n";
				success = true;
				break;
			}
		}
		if (success)
		{
			break;
		}
		else
		{
			cout << "다시 입력하십시오: ";
		}
	}
	cout << "프로그램을 종료합니다.\n";

	return 0;
}