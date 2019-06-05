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
	std::cout << "이름을 입력하시오: ";
	while ((ch = std::cin.get()) != '\n')
	{
		g.fullname[i++] = ch;
	}
	g.fullname[i] = '\0';

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
	std::cout << "이름 : " << g.fullname
		<< ", 핸디캡 : " << g.handicap << std::endl;
}
