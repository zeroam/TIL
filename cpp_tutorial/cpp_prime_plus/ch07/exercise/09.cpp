#include "09.h"
#include <iostream>

namespace num9
{
	void program()
	{
		using std::cout;
		using std::cin;

		cout << "학급의 학생수를 입력하십시오: ";
		int class_size;
		cin >> class_size;
		while (cin.get() != '\n')
			continue;

		student* ptr_stu = new student[class_size];
		int entered = getinfo(ptr_stu, class_size);
		for (int i = 0; i < entered; i++)
		{
			display1(ptr_stu[i]);
			display2(&ptr_stu[i]);
		}
		display3(ptr_stu, entered);
		cout << "프로그램을 종료합니다.\n";
	}

	int getinfo(student pa[], int n)
	{
		int i;
		char ch;
		for (i = 0; i < n; i++)
		{
			std::cout << "학생 " << i + 1 << ":\n";
			std::cout << "이름: ";
			int count = 0;
			while ((ch = std::cin.get()) != '\n')
			{
				if (ch == ' ' || ch == '\t')
					continue;
				pa[i].fullname[count] = ch;
				count++;
			}
			if (count == 0)
				break;
			else
				pa[i].fullname[count] = '\0';

			std::cout << "취미: ";
			std::cin >> pa[i].hobby;

			std::cout << "레벨: ";
			std::cin >> pa[i].ooplevel;
			while (std::cin.get() != '\n')
				continue;

			std::cout << std::endl;
		}
		return i;
	}

	void display1(student st)
	{
		std::cout << "학생 정보\n";
		std::cout << "이름: " << st.fullname << std::endl;
		std::cout << "취미: " << st.hobby << std::endl;
		std::cout << "레벨: " << st.ooplevel << std::endl;
	}

	void display2(const student* ps)
	{
		std::cout << "학생 정보\n";
		std::cout << "이름: " << ps->fullname << std::endl;
		std::cout << "취미: " << ps->hobby << std::endl;
		std::cout << "레벨: " << ps->ooplevel << std::endl;
	}

	void display3(const student pa[], int n)
	{
		for (int i = 0; i < n; i++)
		{
			display2(&pa[i]);
		}
	}
}