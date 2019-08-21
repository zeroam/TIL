#include <cassert>
#include "stack1.h"

int main()
{
	Stack s1;
	assert(s1.isempty() == true);
	assert(s1.isfull() == false);

	Item temp;
	assert(s1.pop(temp) == false);

	for (Item i = 0; i < 10; i++)
	{
		temp = i + 1;
		assert(s1.push(temp) == true);
	}
	
	temp = 20;
	assert(s1.push(temp) == false);

	for (Item i = 0; i < 10; i++)
	{
		assert(s1.pop(temp) == true);
		assert(temp == 10 - i);
	}

	assert(s1.pop(temp) == false);

	Stack s2(20);
	for (Item i = 0; i < 20; i++)
	{
		temp = i + 1;
		assert(s2.push(temp) == true);
	}

	temp = 20;
	assert(s2.push(temp) == false);

	for (Item i = 0; i < 20; i++)
	{
		assert(s2.pop(temp) == true);
		assert(temp == 20 - i);
	}

	assert(s2.pop(temp) == false);
}