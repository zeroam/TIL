// string2.h
#pragma once
#include <iostream>

class String
{
public:
	// �����ڿ� ��Ÿ �޼���
	String(const char* str);
	String();
	String(const String& other);
	~String();
	size_t length() const { return mLen; }
	void stringlow();
	void stringup();
	int has(const char ch) const;

	// �����ε� ������ �޼���
	String& operator=(const String& rhs);
	String& operator=(const char* str);
	char& operator[](int index);
	const char& operator[](int index) const;

	// �����ε� ������ ������
	friend String operator+(const String& lhs, const String& rhs);
	friend bool operator<(const String& lhs, const String& rhs);
	friend bool operator>(const String& lhs, const String& rhs);
	friend bool operator==(const String& lhs, const String& rhs);
	friend std::ostream& operator<<(std::ostream& os, const String& rhs);
	friend std::istream& operator>>(std::istream& is, String& rhs);

	// static �Լ�
	static size_t HowMany();

private:
	char* mStr;						// ���ڿ��� �����ϴ� ������
	size_t mLen;						// ���ڿ� ����
	static int numStrings;			// ��ü�� ��
	static const int CINLIM = 80;	// cin �Է� �Ѱ�
};