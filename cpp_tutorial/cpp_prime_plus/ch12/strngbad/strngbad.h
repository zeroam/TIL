// strngbad.h -- ������ �ִ� string Ŭ���� ����
#pragma once
#include <iostream>

class StringBad
{
public:
	StringBad(const char* s);	// ������
	StringBad();				// ����Ʈ ������
	StringBad(const StringBad& other);	// ���� ������
	~StringBad();				// �ı���

	StringBad& operator=(const StringBad& rhs);	// ���� ������
	
	// ������ �Լ�
	friend std::ostream& operator<<(std::ostream& os, const StringBad& st);

private:
	char* str;					// ���ڿ��� �����ϴ� ������
	int len;					// ���ڿ� ����
	static int num_strings;		// ��ü�� ��
};
