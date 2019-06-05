#include "07.h"
#include <iostream>

void num7::program()
{
	using namespace std;

	cout << "단어들을 입력하시오 (끝내려면 q) : \n";
	int consonant = 0;
	int vowel = 0;
	int etc = 0;
	char word[20];
	while ((cin >> word))
	{
		if (memcmp(word, "q", 2) == 0)
			break;

		if (isalpha(word[0]))
		{
			switch (tolower(word[0]))
			{
			case 'a':
			case 'e':
			case 'i':
			case 'o':
			case 'u':
				vowel++;
				break;
			default:
				consonant++;
			}
		}
		else
		{
			etc++;
		}
	}
	
	cout << "모음으로 시작하는 단어 수: " << vowel << endl;
	cout << "자음으로 시작하는 단어 수: " << consonant << endl;
	cout << "기타: " << etc;
}
