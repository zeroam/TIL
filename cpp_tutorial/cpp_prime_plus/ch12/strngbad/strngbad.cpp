// strngbad.cpp -- StringBad Ŭ������ �޼���
#include <cstring>
#include "strngbad.h"

using std::cout;

// static Ŭ���� ����� �ʱ�ȭ �Ѵ�
int StringBad::num_strings = 0;

// Ŭ���� �޼���

// C ��Ÿ���� ���ڿ��κ��� StringBad�� �����Ѵ�
StringBad::StringBad(const char* s)
{
	len = std::strlen(s);			// ���ڿ��� ũ�⸦ ����
	str = new char[len + 1];		// ��� ������ �����Ѵ�
	std::memcpy(str, s, len + 1);	// �����͸� �ʱ�ȭ �Ѵ�
	num_strings++;					// ������ ��ü ���� ī��Ʈ�Ѵ�
	cout << num_strings << ": \"" << str
		<< "\" ��ü ����\n";		// ������ �޽���
}

StringBad::StringBad()				// ����Ʈ ������
{
	len = 3;
	str = new char[len + 1];
	std::memcpy(str, "C++", len + 1);
	num_strings++;
	cout << num_strings << ": \"" << str
		<< "\" ����Ʈ ��ü ����\n";	// ������ �޽���
}

StringBad::StringBad(const StringBad& other)
	: len(other.len)
{
	str = new char[len + 1];
	std::memcpy(str, other.str, len + 1);
	num_strings++;
	cout << "���� ������ ȣ��\n";
}

StringBad::~StringBad()				// �� �ʿ��� �ı���
{
	cout << "\"" << str << "\" ��ü �ı�, ";			// ������ �޽���
	--num_strings;										// �ʿ��ϴ�
	cout << "���� ��ü ��: " << num_strings << "\n";	// ������ �޽���
	delete[] str;										// �ʿ��ϴ�
}

StringBad& StringBad::operator=(const StringBad& rhs)
{
	if (this == &rhs)
	{
		return *this;
	}

	delete[] str;

	len = rhs.len;
	str = new char[len + 1];
	std::memcpy(str, rhs.str, len + 1);

	cout << "���� ������ ȣ��\n";

	return *this;
}

std::ostream& operator<<(std::ostream& os, const StringBad& st)
{
	os << st.str;
	return os;
}
