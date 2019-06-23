#include <iostream>
#include <cassert>
#include "LinkedList.h"


int main()
{
	LinkedList list;
	assert(list.IsEmpty() == true);
	assert(list.IsFull() == false);

	int a = 3;
	list.Append(a);
	list.Append(4);
	assert(list.Size() == 2);
	assert(list.IsFull() == false);
	assert(list.IsEmpty() == false);


	std::cout << list << std::endl;

	list.Append(5);
	list.Append(6);
	list.Insert(0, 7);
	list.Insert(1, 6);

	std::cout << list << std::endl;

	list.Remove(0);
	list.Remove(2);

	std::cout << list << std::endl;

	list.Append(1);
	list.Append(2);
	list.Append(3);
	list.Append(4);
	list.Append(5);
	list.Append(6);
	assert(list.IsFull() == true);

	std::cout << list << std::endl;

	assert(list.Append(7) == false);

	return 0;
}