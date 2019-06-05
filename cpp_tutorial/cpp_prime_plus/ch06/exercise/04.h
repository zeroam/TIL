#pragma once

namespace num4
{
	int const STR_SIZE = 80;
	
	void program();
	
	// Benevolent Order of Programmers ȸ�� ����ü
	enum name
	{
		fullname, title, bopname, pref
	};
	struct bop {
		char fullname[STR_SIZE];		// �Ǹ�
		char title[STR_SIZE];			// ����
		char bopname[STR_SIZE];			// BOP ���̵�
		int preference;					// 0 = fullname, 1 = title, 2 = bopname
	};

	void printBop(bop* boparr, int size, int preference);
}
