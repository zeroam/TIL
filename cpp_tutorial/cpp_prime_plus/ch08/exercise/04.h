#pragma once

namespace num4
{
	void program();

	struct stringy
	{
		char* str;		// ���ڿ��� �����Ѵ�
		int ct;			// ���ڿ��� ����('\0'�� ����)
	};

	void set(stringy& str, const char* src);
	void show(const stringy& str, int size = 1);
	void show(const char* str, int size = 1);
}
