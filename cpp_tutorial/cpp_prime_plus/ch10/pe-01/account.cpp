#include "account.h"
#include <iostream>

// ������ : ����Ʈ ������ x
BankAccount::BankAccount(const char* client, const char* num, double bal)
	: mBalance(bal)
{
	std::cout << "������ ȣ��\n";
	std::cout << "bal ��: " << bal << std::endl;
	memcpy(mName, client, NAME_SIZE - 1);
	mName[NAME_SIZE - 1] = '\0';
	memcpy(mAcctnum, num, ACCOUNT_SIZE - 1);
	mAcctnum[ACCOUNT_SIZE - 1] = '\0';
}

// ���� ������
BankAccount::BankAccount(const BankAccount& other)
	: BankAccount(other.mName, other.mAcctnum, other.mBalance)
{
	std::cout << "���� ������ ȣ��\n";
}

// �Ҹ���
BankAccount::~BankAccount()
{
	std::cout << "�Ҹ��� ȣ��\n";
}

// ���� ������ �����ε�
BankAccount& BankAccount::operator=(const BankAccount& rhs)
{
	std::cout << "���� ������ ȣ��\n";
	if (this == &rhs)
	{
		std::cout << "���� ��ü �Դϴ�.";
		return *this;
	}

	memcpy(mName, rhs.mName, NAME_SIZE - 1);
	mName[NAME_SIZE - 1] = '\0';
	memcpy(mAcctnum, rhs.mAcctnum, ACCOUNT_SIZE - 1);
	mAcctnum[ACCOUNT_SIZE - 1] = '\0';
	mBalance = rhs.mBalance;

	return *this;
}

void BankAccount::Show() const
{
	std::cout << "���� ���� ���\n";
	std::cout << "  �� : " << mName << std::endl;
	std::cout << "  ���� : " << mAcctnum << std::endl;
	std::cout << "  �ܾ� : " << mBalance << std::endl;
}

void BankAccount::Deposit(double cash)
{
	mBalance += cash;
}

void BankAccount::Withdraw(double cash)
{
	mBalance -= cash;
}
