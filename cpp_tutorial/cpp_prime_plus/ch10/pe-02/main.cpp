#include "person.h"
#include <iostream>

int main()
{
	Person one;						// 디폴트 생성자 호출
	Person two("Smythecraft");		// 명시적으로 생성자 호출, 디폴트 매개변수 사용
	Person three("Dimwiddy", "Sam");

	one.Show();
	one.FormalShow();

	two.Show();
	two.FormalShow();

	three.Show();
	three.FormalShow();

	return 0;
}