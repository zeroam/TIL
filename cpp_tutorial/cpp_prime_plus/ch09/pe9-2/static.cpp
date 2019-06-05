// static.cpp -- 정적 지역 변수 사용하기
#include <iostream>
#include <string>
// 상수
const int ArSize = 10;

// 함수 원형
void strcount(std::string str);

int main()
{
	using namespace std;
	std::string input;

	cout << "영문으로 한 행을 입력하십시오:\n";
	getline(std::cin, input);
	while (input != "")
	{
		strcount(input);
		cout << "다음 행을 입력하십시오(끝내려면 빈 행을 입력):\n";
		getline(std::cin, input);
	}
	cout << "프로그램을 종료합니다.\n";
	return 0;
}

void strcount(std::string str)
{
	using namespace std;
	static int total = 0;		// 정적 지역 변수
	int count = 0;				// 자동 지역 변수

	cout << "\"" << str << "\"에는 ";
	count = str.length();
	total += count;
	cout << count << "개의 문자가 있습니다.\n";
	cout << "지금까지 총 " << total << "개의 문자를 입력하셨습니다.\n";
}