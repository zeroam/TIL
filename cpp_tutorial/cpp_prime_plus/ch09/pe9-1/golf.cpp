#include "golf.h"
#include <iostream>

void setgolf(golf& g, const char* name, int hc)
{
	int i = 0;
	while (*(name + i) != '\0')
	{
		g.fullname[i] = *(name + i);
		i++;
	}
	g.fullname[i] = '\0';

	g.handicap = hc;
}

int setgolf(golf& g)
{
	char ch;
	int i = 0;
	std::cout << "�̸��� �Է��Ͻÿ�: ";
	while ((ch = std::cin.get()) != '\n')
	{
		g.fullname[i++] = ch;
	}
	g.fullname[i] = '\0';

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
			g.handicap = num;
			break;
		}
	}

	return 1;
}

void handicap(golf& f, int hc)
{
	f.handicap = hc;
}

void showgolf(const golf& g)
{
	std::cout << "�̸� : " << g.fullname
		<< ", �ڵ�ĸ : " << g.handicap << std::endl;
}
