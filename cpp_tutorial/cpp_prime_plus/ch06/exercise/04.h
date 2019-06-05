#pragma once

namespace num4
{
	int const STR_SIZE = 80;
	
	void program();
	
	// Benevolent Order of Programmers 회원 구조체
	enum name
	{
		fullname, title, bopname, pref
	};
	struct bop {
		char fullname[STR_SIZE];		// 실명
		char title[STR_SIZE];			// 직함
		char bopname[STR_SIZE];			// BOP 아이디
		int preference;					// 0 = fullname, 1 = title, 2 = bopname
	};

	void printBop(bop* boparr, int size, int preference);
}
