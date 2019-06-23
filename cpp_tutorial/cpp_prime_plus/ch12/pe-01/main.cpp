#include <iostream>
#include "cow.h"

int main()
{
	// 디폴트 생성자 호출
	Cow cow;
	cow.ShowCow();

	Cow* pcow = new Cow;
	pcow->ShowCow();

	// 생성자 호출
	Cow cow2("cow2", "drinking", 35);
	cow2.ShowCow();

	Cow* pcow2 = new Cow("pcow2", "talking", 85);
	pcow2->ShowCow();

	// 복사 생성자 호출
	Cow cow3(cow2);
	Cow cow4 = cow2;

	cow3.ShowCow();
	cow4.ShowCow();

	Cow* pcow3 = new Cow(cow2);
	pcow3->ShowCow();

	// 대입 연산자 호출
	Cow temp;
	temp = cow2;
	temp.ShowCow();

	Cow* ptemp;
	ptemp = &cow2;
	ptemp->ShowCow();

	// 소멸자 호출
	delete pcow;
	delete pcow2;
	delete pcow3;

	return 0;
}