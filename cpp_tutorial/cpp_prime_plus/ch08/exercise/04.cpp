#include "04.h"
#include <iostream>

namespace num4
{
	void program()
	{
		stringy beany;
		char testing[] = "Reality isn't what it used to be";

		set(beany, testing);
			// ù��° �Ű������� �����̴�,
			// testing�� �纻�� ������ ������ �����Ѵ�,
			// beany�� str ����� �� ����� �����ϵ��� �����Ѵ�,
			// testing�� �� ��Ͽ� �����Ѵ�,
			// beany�� ct ����� �����Ѵ�
		show(beany);		// ���ڿ� ����� �� �� ����Ѵ�
		show(beany, 2);		// ���ڿ� ����� �� �� ����Ѵ�
		testing[0] = 'D';
		testing[1] = 'u';
		show(testing);		// testing ���ڿ��� �� �� ����Ѵ�
		show(testing, 3);	// testing ���ڿ��� �� �� ����Ѵ�
		show("Done");
	}

	void set(stringy& str, const char* src)
	{
		str.ct = 0;
		while (*(src + str.ct))
		{
			str.ct++;
		}
		str.str = new char[str.ct + 1];
		for (int i = 0; i < str.ct + 1; i++)
		{
			str.str[i] = src[i];
		}
	}

	void show(const stringy& str, int size)
	{
		for (int i = 0; i < size; i++)
		{
			std::cout << str.str << std::endl;
		}
	}

	void show(const char* str, int size)
	{
		for (int i = 0; i < size; i++)
		{
			std::cout << str << std::endl;
		}
	}
}