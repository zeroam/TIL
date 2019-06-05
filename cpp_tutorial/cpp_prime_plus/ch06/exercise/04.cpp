#include "04.h"
#include <iostream>
#include <iomanip>

namespace num4 {
	void program()
	{
		using namespace std;

		bop name_list[5] =
		{
			{"Wimp Macho", "Macho", "MC", fullname},
			{"Raki Rhodes", "Raki", "RK", title},
			{"Celia Laiter", "Celia", "CL", bopname},
			{"Hoppy Hipman", "Hoppy", "HH", fullname},
			{"Pat Hand", "Pat", "PH", bopname}
		};

		cout << left;
		cout << "Benevolent Order of Programmers" << endl;
		cout << setw(30) << "a. 실명으로 열람" << "b. 직함으로 열람\n";
		cout << setw(30) << "c. BOP 아이디로 열람" << "d. 회원이 지정한 것으로 열람\n";
		cout << "q. 종료\n";
		cout << "원하는 것을 선택하십시오: ";

		char ch;

		while ((ch = cin.get()) != 'q')
		{
			switch(ch)
			{
			case 'a':
				printBop(name_list, 5, fullname);
				break;
			case 'b':
				printBop(name_list, 5, title);
				break;
			case 'c':
				printBop(name_list, 5, bopname);
				break;
			case 'd':
				printBop(name_list, 5, pref);
				break;
			default:
				cout << "a, b, c, d 중에 하나를 선택하십시오 (종료는 q) : ";
				break;
			}
		}


	}
	void printBop(bop* boparr, int size, int preference)
	{
		using std::cout;

		bool pref_flag = false;
		if (preference == pref)
		{
			pref_flag = true;
		}

		for (int i = 0; i < size; i++)
		{
			if (pref_flag)
				preference = boparr[i].preference;

			switch (preference)
			{
			case fullname:
				cout << boparr[i].fullname << "\n";
				break;
			case title:
				cout << boparr[i].title << "\n";
				break;
			case bopname:
				cout << boparr[i].bopname << "\n";
				break;
			}
		}

		

	}
}
