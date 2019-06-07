// or.cpp -- 논리합 연산자
#include <iostream>
int main()
{
	using namespace std;
	cout << "이 프로그램은 하드 디스크를 다시 포맷합니다.\n"
		"하드 디스크에 있는 모든 데이터가 지워집니다.\n"
		"계속하시겠습니까? <y/n> ";
	char ch;
	cin >> ch;
	if (ch == 'y' || ch == 'Y')
		cout << "당신에게 분명히 경고를 했습니다.\a\a\n";
	else if (ch == 'n' || ch == 'N')
		cout << "현명한 선택입니다. 프로그램을 종료합니다.\n";
	else
		cout << "y나 n을 입력하지 않았습니다.\n"
		"지시사항을 따를수 없습니다."
		"휴지통을 비우고 디스크를 정리하겠습니다.\n";

	return 0;
}