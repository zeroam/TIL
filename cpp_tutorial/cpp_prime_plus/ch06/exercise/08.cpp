#include "08.h"
#include <iostream>
#include <fstream>
#include <string>

void num8::program()
{
	using namespace std;

	ifstream inFile;
	inFile.open("test.txt");
	if (!inFile.is_open())
	{
		cout << "파일을 읽을 수 없습니다.\n프로그램을 종료합니다.";
		return;
	}

	char ch;
	int count = -1;
	while (!inFile.eof())
	{
		if (inFile.fail())
		{
			cout << "데이터 불일치로 입력이 종료되었습니다.\n";
			break;
		}
		count++;
		inFile.get(ch);
	}
	inFile.close();
	cout << "문자수는 총 " << count << "자 입니다.";
}