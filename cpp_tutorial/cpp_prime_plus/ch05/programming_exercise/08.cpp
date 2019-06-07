#include "08.h"
#include <iostream>
#include <cstring>

void num8::program()
{
	using std::cout;
	using std::cin;
	using std::endl;

	char words[20];
	int count = 0;
	cout << "영어 단어들을 입력하십시오 (끝내려면 done을 입력) :" << endl;
	
	while (!cin.fail())
	{
		cin >> words;
		if (strcmp(words, "done") == 0)
			break;
		count++;
	}

	cout << "총 " << count << " 단어가 입력되었습니다.";
}
