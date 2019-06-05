#include "04.h"
#include <iostream>

namespace num4
{
	void program()
	{
		stringy beany;
		char testing[] = "Reality isn't what it used to be";

		set(beany, testing);
			// 첫번째 매개변수는 참조이다,
			// testing의 사본을 저장할 공간을 대입한다,
			// beany의 str 멤버가 새 블록을 지시하도록 설정한다,
			// testing을 새 블록에 복사한다,
			// beany의 ct 멤버를 설정한다
		show(beany);		// 문자열 멤버를 한 번 출력한다
		show(beany, 2);		// 문자열 멤버를 두 번 출력한다
		testing[0] = 'D';
		testing[1] = 'u';
		show(testing);		// testing 문자열을 한 번 출력한다
		show(testing, 3);	// testing 문자열을 세 번 출력한다
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