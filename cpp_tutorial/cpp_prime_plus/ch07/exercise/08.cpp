#include "08.h"
#include <iostream>

namespace num8
{
	const char* Sname[] = { "Spring", "Summer", "Fall", "Winter" };
	void program1()
	{
		std::array<double, Seasons> expenses;
		fill(&expenses);
		show(expenses);
	}

	void program2()
	{
		Exp expenses;
		fill(&expenses);
		show(expenses);
	}

	void fill(std::array<double, Seasons>* pa)
	{
		using namespace std;
		for (int i = 0; i < Seasons; i++)
		{
			cout << Sname[i] << "에 소요되는 비용:";
			cin >> (*pa)[i];
		}
	}

	void fill(Exp* pa)
	{
		using namespace std;
		for (int i = 0; i < Seasons; i++)
		{
			cout << Sname[i] << "에 소요되는 비용:";
			cin >> pa->expenses[i];
		}
	}

	void show(std::array<double, Seasons> da)
	{
		using namespace std;
		double total = 0.0;
		cout << "\n계절별 비용\n";
		for (int i = 0; i < Seasons; i++)
		{
			cout << Sname[i] << " : $" << da[i] << endl;
			total += da[i];
		}
		cout << "총 비용 : $" << total << endl;
	}

	void show(Exp da)
	{
		using namespace std;
		double total = 0.0;
		cout << "\n계절별 비용\n";
		for (int i = 0; i < Seasons; i++)
		{
			cout << Sname[i] << " : $" << da.expenses[i] << endl;
			total += da.expenses[i];
		}
		cout << "총 비용 : $" << total << endl;
	}
}