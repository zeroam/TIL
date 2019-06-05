#include "01.h"
#include <iostream>
#include <cctype>

void num1::program()
{
	using namespace std;

	char ch;
	while ((ch = cin.get()) != '@')
	{
		if (isupper(ch))
			ch = tolower(ch);
		else if (islower(ch))
			ch = toupper(ch);

		cout << ch;
	}
	cout << endl;
}
