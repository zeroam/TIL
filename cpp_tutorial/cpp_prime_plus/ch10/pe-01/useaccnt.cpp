#include "account.h"
#include <iostream>

int main()
{
	std::cout << std::fixed;
	std::cout.precision(2);

	// ������ ȣ��
	BankAccount jone("jone", "123-456-789");
	std::cout << "jone �ּ�: " << &jone << std::endl;
	jone.Deposit(1000000);
	jone.Show();

	// ���� ������ ȣ��
	BankAccount park = jone;
	park.Withdraw(50000);
	std::cout << "park �ּ� : " << &park << std::endl;
	std::cout << "park ��� :\n";
	park.Show();
	std::cout << "jone ��� :\n";
	jone.Show();


	// �׳� �ּҰ� ����
	BankAccount* ptr = new BankAccount();
	//ptr = &park;
	//ptr->Show();
	//std::cout << "ptr �ּ� : " << ptr << std::endl;

	// ���� ������?
	std::cout << "jone �ּ�: " << &jone << std::endl;
	*ptr = jone;
	ptr->Withdraw(100000);
	std::cout << "ptr �ּ� : " << ptr << std::endl;
	std::cout << "ptr ��� :\n";
	ptr->Show();
	std::cout << "park ��� :\n";
	park.Show();

	return 0;
}