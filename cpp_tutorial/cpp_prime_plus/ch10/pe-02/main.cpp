#include "person.h"
#include <iostream>

int main()
{
	Person one;						// ����Ʈ ������ ȣ��
	Person two("Smythecraft");		// ��������� ������ ȣ��, ����Ʈ �Ű����� ���
	Person three("Dimwiddy", "Sam");

	one.Show();
	one.FormalShow();

	two.Show();
	two.FormalShow();

	three.Show();
	three.FormalShow();

	return 0;
}