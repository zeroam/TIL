#include "01.h"
#include <iostream>

namespace num1
{
	void program()
	{
		using namespace std;
		const char* str = "Hello, World";
		
		cout << "1�� ���:" << endl;
		print_chars(str);

		cout << "5�� ���:\n";
		print_chars(str, 5);
	}

	void print_chars(const char* ptr)
	{
		std::cout << ptr << std::endl;
	}

	void print_chars(const char* ptr, int num)
	{
		if (num <= 0)
		{
			return;
		}

		for (int i = 0; i < num; i++)
		{
			print_chars(ptr);
		}
	}
}