#include "golf.h"
#include <iostream>

Golf::Golf(const char* name, int hc)
	: mHandicap(hc)
{
	memcpy(mFullName, name, LEN - 1);
	mFullName[LEN - 1] = '\0';
}

int Golf::SetGolf()
{
	char ch;
	int i = 0;
	std::cout << "이름을 입력하시오: ";
	while ((ch = std::cin.get()) != '\n')
	{
		this->mFullName[i++] = ch;
	}
	this->mFullName[i] = '\0';

	if (i == 0)
	{
		std::cout << "빈문자열을 입력하셨습니다.\n";
		return 0;
	}

	int num;
	std::cout << "핸디캡을 입력하십시오: ";
	while (true)
	{
		std::cin >> num;
		if (std::cin.fail())
		{
			std::cin.clear();
			while ((ch = std::cin.get()) != '\n')
			{
				continue;
			}
			std::cout << "숫자를 입력하십시오 : ";
		}
		else
		{
			this->mHandicap = num;
			break;
		}
	}

	return 1;
}

void Golf::ShowGolf()
{
	std::cout << "이름 : " << this->mFullName
		<< ", 핸디캡 : " << this->mHandicap << std::endl;
}