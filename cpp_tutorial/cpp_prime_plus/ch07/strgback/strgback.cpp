// strgback.cpp -- char형을 지시하는 포인터를 리턴하는 함수
#include <iostream>
char* buildstr(char c, int n);
int main()
{
	using namespace std;
	int times;
	char ch;

	cout << "문자를 하나 입력하십시오: ";
	cin >> ch;
	cout << "정수를 하나 입력하십시오: ";
	cin >> times;
	char* ps = buildstr(ch, times);
	cout << ps << endl;
	delete[] ps;
	ps = buildstr('+', 20);
	cout << ps << "-DONE-" << ps << endl;
	delete[] ps;

	return 0;
}

// n개의 문자 c로 이루어진 문자열을 만든다
char* buildstr(char c, int n)
{
	char* pstr = new char[n + 1];
	pstr[n] = '\0';
	while (n-- > 0)
		pstr[n] = c;
	return pstr;
}