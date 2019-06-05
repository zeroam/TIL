#pragma once

namespace num9
{
	const int SLEN = 30;
	struct student
	{
		char fullname[SLEN];
		char hobby[SLEN];
		int ooplevel;
	};

	void program();

	int getinfo(student pa[], int n);

	void display1(student st);
	void display2(const student* ps);
	void display3(const student pa[], int n);
}
