#include "09.h"
#include <iostream>
#include <string>

void num9::program()
{
	using std::cout;
	using std::cin;
	using std::endl;

	std::string words;
	int count = 0;
	cout << "영어 단어들을 입력하십시오 (끝내려면 done을 입력) :" << endl;

	while (!cin.fail())
	{
		cin >> words;
		if (words == "done")
			break;
		count++;
	}

	cout << "총 " << count << " 단어가 입력되었습니다.";
}
