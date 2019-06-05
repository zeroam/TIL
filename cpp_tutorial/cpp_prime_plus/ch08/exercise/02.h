#pragma once

namespace num2
{
	struct CandyBar
	{
		char name[30];
		double weight;
		int cal;
	};

	void program();

	CandyBar& SetCandyBar(
		CandyBar& candybar, 
		const char* name = "Millennium Munch",
		double weight = 2.85,
		int cal = 350);

	void ShowCandyBar(CandyBar candybar);
	void Strcpy(char* dest, const char* src);
}
