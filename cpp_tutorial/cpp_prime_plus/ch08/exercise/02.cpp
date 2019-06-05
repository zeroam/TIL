#include "02.h"
#include <iostream>

namespace num2
{
	void program()
	{
		CandyBar c1;
		CandyBar c2;

		SetCandyBar(c1);
		SetCandyBar(c2, "Nice Candy", 3.5, 270);

		ShowCandyBar(c1);
		ShowCandyBar(c2);
	}

	CandyBar& SetCandyBar(CandyBar& candybar, const char* name, double weight, int cal)
	{
		Strcpy(candybar.name, name);
		candybar.weight = weight;
		candybar.cal = cal;

		return candybar;
	}

	void ShowCandyBar(CandyBar candybar)
	{
		using std::cout;
		using std::endl;

		cout << "Äµµð¹Ù ÀÌ¸§: " << candybar.name << endl;
		cout << "Äµµð¹Ù ¹«°Ô: " << candybar.weight << endl;
		cout << "Äµµð¹Ù ¿­·®: " << candybar.cal << endl;
	}

	void Strcpy(char* dest, const char* src)
	{
		while (*src)
		{
			*dest = *src;
			src++;
			dest++;
		}
		*dest = '\0';
	}
}