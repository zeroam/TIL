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
	std::cout << "�̸��� �Է��Ͻÿ�: ";
	while ((ch = std::cin.get()) != '\n')
	{
		this->mFullName[i++] = ch;
	}
	this->mFullName[i] = '\0';

	if (i == 0)
	{
		std::cout << "���ڿ��� �Է��ϼ̽��ϴ�.\n";
		return 0;
	}

	int num;
	std::cout << "�ڵ�ĸ�� �Է��Ͻʽÿ�: ";
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
			std::cout << "���ڸ� �Է��Ͻʽÿ� : ";
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
	std::cout << "�̸� : " << this->mFullName
		<< ", �ڵ�ĸ : " << this->mHandicap << std::endl;
}