#include "account.h"
#include <iostream>

int main()
{
	std::cout << std::fixed;
	std::cout.precision(2);

	// 생성자 호출
	BankAccount jone("jone", "123-456-789");
	std::cout << "jone 주소: " << &jone << std::endl;
	jone.Deposit(1000000);
	jone.Show();

	// 복사 생성자 호출
	BankAccount park = jone;
	park.Withdraw(50000);
	std::cout << "park 주소 : " << &park << std::endl;
	std::cout << "park 출력 :\n";
	park.Show();
	std::cout << "jone 출력 :\n";
	jone.Show();


	// 그냥 주소값 대입
	BankAccount* ptr = new BankAccount();
	//ptr = &park;
	//ptr->Show();
	//std::cout << "ptr 주소 : " << ptr << std::endl;

	// 대입 연산자?
	std::cout << "jone 주소: " << &jone << std::endl;
	*ptr = jone;
	ptr->Withdraw(100000);
	std::cout << "ptr 주소 : " << ptr << std::endl;
	std::cout << "ptr 출력 :\n";
	ptr->Show();
	std::cout << "park 출력 :\n";
	park.Show();

	return 0;
}