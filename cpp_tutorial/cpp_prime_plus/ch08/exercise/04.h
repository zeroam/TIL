#pragma once

namespace num4
{
	void program();

	struct stringy
	{
		char* str;		// 문자열을 지시한다
		int ct;			// 문자열의 길이('\0'은 제외)
	};

	void set(stringy& str, const char* src);
	void show(const stringy& str, int size = 1);
	void show(const char* str, int size = 1);
}
