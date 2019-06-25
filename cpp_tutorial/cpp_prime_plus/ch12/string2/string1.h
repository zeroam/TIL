// string1.h -- Ȯ�� ������ String Ŭ���� ����
#pragma once
#include <iostream>

class String
{
public:
	// �����ڿ� ��Ÿ �޼���
	String(const char* s);				// ������
	String();							// ����Ʈ ������
	String(const String& st);			// ���� ������
	~String();							// �ı���
	int length() const { return len; }

	// �����ε� ������ �޼���
	String& operator=(const String& st);
	String& operator=(const char* s);
	char& operator[](int i);
	const char& operator[](int i) const;

	// �����ε� ������ ������
	friend bool operator<(const String& st1, const String& st2);
	friend bool operator>(const String& st1, const String& st2);
	friend bool operator==(const String& st1, const String& st2);
	friend std::ostream& operator<<(std::ostream& os, const String& st);
	friend std::istream& operator>>(std::istream& is, String& st);

	// static �Լ�
	static int HowMany();

private:
	char* str;							// ���ڿ��� �����ϴ� ������
	int len;							// ���ڿ��� ����
	static int num_strings;				// ��ü�� ��
	static const int CINLIM = 80;		// cin �Է� �Ѱ�
};
