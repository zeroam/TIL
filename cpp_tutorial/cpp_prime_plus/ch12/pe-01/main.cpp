#include <iostream>
#include "cow.h"

int main()
{
	// ����Ʈ ������ ȣ��
	Cow cow;
	cow.ShowCow();

	Cow* pcow = new Cow;
	pcow->ShowCow();

	// ������ ȣ��
	Cow cow2("cow2", "drinking", 35);
	cow2.ShowCow();

	Cow* pcow2 = new Cow("pcow2", "talking", 85);
	pcow2->ShowCow();

	// ���� ������ ȣ��
	Cow cow3(cow2);
	Cow cow4 = cow2;

	cow3.ShowCow();
	cow4.ShowCow();

	Cow* pcow3 = new Cow(cow2);
	pcow3->ShowCow();

	// ���� ������ ȣ��
	Cow temp;
	temp = cow2;
	temp.ShowCow();

	Cow* ptemp;
	ptemp = &cow2;
	ptemp->ShowCow();

	// �Ҹ��� ȣ��
	delete pcow;
	delete pcow2;
	delete pcow3;

	return 0;
}