#include "03.h"
#include <iostream>
#include <iomanip>

void num3::program()
{
	using namespace std;
	cout << "다음 선택 사항 중에서 하나를 선택하십시오. (끝내려면 q)" << endl;
	cout << left;
	cout << setw(20) << "c) camera" << "p) pianist\n";
	cout << setw(20) << "t) tree" << "g) game\n";

	char ch;
	while ((ch = cin.get()) != 'q')
	{
		switch (ch)
		{
		case 'c':
			cout << "카메라 출력\n";
			break;
		case 'p':
			cout << "피아니스트 출력\n";
			break;
		case 't':
			cout << "나무 출력\n";
			break;
		case 'g':
			cout << "게임 출력\n";
			break;
		case ' ':
		case '\t':
		case '\n':
			break;
		default:
			cout << "c, p, t, g 중에서 하나를 선택하십시오.(끝내려면 q) : ";
			break;
		}
	}
}
