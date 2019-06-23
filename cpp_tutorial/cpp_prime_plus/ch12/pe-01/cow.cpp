#include <iostream>
#include "cow.h"

Cow::Cow()
	: weight(0)
{
	std::cout << "����Ʈ ������ ȣ��\n";
	name[0] = '\0';
	hobby = new char[1];
	hobby[0] = '\0';
}


Cow::Cow(const char* nm, const char* ho, double weight)
	: weight(weight)
{
	std::cout << "������ ȣ��\n";
	memcpy(name, nm, strlen(nm) + 1);
	
	hobby = new char[strlen(ho) + 1];
	memcpy(hobby, ho, strlen(ho) + 1);
}

Cow::Cow(const Cow& other)
	: weight(other.weight)
{
	std::cout << "���� ������ ȣ��\n";
	memcpy(name, other.name, strlen(other.name) + 1);

	hobby = new char[strlen(other.hobby) + 1];
	memcpy(hobby, other.hobby, strlen(other.hobby) + 1);
}

Cow::~Cow()
{
	std::cout << name << ": �ı��� ȣ��\n";
	delete[] hobby;
}

Cow& Cow::operator=(const Cow& rhs)
{
	std::cout << "���� ������ ȣ��\n";
	if (this == &rhs)
	{
		return *this;
	}

	delete[] hobby;

	weight = rhs.weight;
	memcpy(name, rhs.name, strlen(rhs.name) + 1);

	hobby = new char[strlen(rhs.hobby) + 1];
	memcpy(hobby, rhs.hobby, strlen(rhs.hobby) + 1);

	return *this;
}

void Cow::ShowCow() const
{
	std::cout << "name: " << name << std::endl;
	std::cout << "hobby: " << hobby << std::endl;
	std::cout << "weight: " << weight << std::endl;
}