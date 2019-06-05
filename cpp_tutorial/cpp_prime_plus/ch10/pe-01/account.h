#pragma once
#include <cstring>

class BankAccount
{
public:
	BankAccount(): mBalance(0) {};
	BankAccount(const char* client, const char* num, double bal = 0.0);
	BankAccount(const BankAccount& other);	// ���� ������
	~BankAccount();

	BankAccount& operator=(const BankAccount& rhs);	// ���� ������

	void Show() const;
	void Deposit(double cash);
	void Withdraw(double cash);

private:
	enum {NAME_SIZE=40, ACCOUNT_SIZE=25};
	char mName[NAME_SIZE];
	char mAcctnum[ACCOUNT_SIZE];
	double mBalance;
};
