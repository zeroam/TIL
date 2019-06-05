#include "account.h"
#include <iostream>

// 생성자 : 디폴트 생성자 x
BankAccount::BankAccount(const char* client, const char* num, double bal)
	: mBalance(bal)
{
	std::cout << "생성자 호출\n";
	std::cout << "bal 값: " << bal << std::endl;
	memcpy(mName, client, NAME_SIZE - 1);
	mName[NAME_SIZE - 1] = '\0';
	memcpy(mAcctnum, num, ACCOUNT_SIZE - 1);
	mAcctnum[ACCOUNT_SIZE - 1] = '\0';
}

// 복사 생성자
BankAccount::BankAccount(const BankAccount& other)
	: BankAccount(other.mName, other.mAcctnum, other.mBalance)
{
	std::cout << "복사 생성자 호출\n";
}

// 소멸자
BankAccount::~BankAccount()
{
	std::cout << "소멸자 호출\n";
}

// 대입 연산자 오버로딩
BankAccount& BankAccount::operator=(const BankAccount& rhs)
{
	std::cout << "대입 연산자 호출\n";
	if (this == &rhs)
	{
		std::cout << "같은 객체 입니다.";
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
	std::cout << "계좌 정보 출력\n";
	std::cout << "  고객 : " << mName << std::endl;
	std::cout << "  계좌 : " << mAcctnum << std::endl;
	std::cout << "  잔액 : " << mBalance << std::endl;
}

void BankAccount::Deposit(double cash)
{
	mBalance += cash;
}

void BankAccount::Withdraw(double cash)
{
	mBalance -= cash;
}
