#include "07.h"
#include <iostream>

void num7::program()
{
	using namespace std;

	cout << "�ܾ���� �Է��Ͻÿ� (�������� q) : \n";
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
	
	cout << "�������� �����ϴ� �ܾ� ��: " << vowel << endl;
	cout << "�������� �����ϴ� �ܾ� ��: " << consonant << endl;
	cout << "��Ÿ: " << etc;
}
