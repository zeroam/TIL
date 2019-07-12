// acctabc.h
#pragma once
#include <iostream>
#include <string>

// �߻�ȭ ���� Ŭ����
class AcctABC
{
public:
	AcctABC(const std::string& s = "Nullbody", long an = -1,
		double bal = 0.0);
	virtual ~AcctABC() { };

	void Deposit(double amt);
	virtual void Withdraw(double amt) = 0;
	double Balance() const { return balance; }
	virtual void ViewAcct() const = 0;

protected:
	struct Formatting
	{
		std::ios_base::fmtflags flag;
		std::streamsize pr;
	};
	const std::string& FullName() const { return fullName; }
	long AcctNum() const { return acctNum; }
	Formatting SetFormat() const;
	void Restore(Formatting& f) const;

private:
	std::string fullName;
	long acctNum;
	double balance;
};

// Brass Account Class
class Brass : public AcctABC
{
public:
	Brass(const std::string& s = "Nullbody", long an = -1,
		double bal = 0.0) : AcctABC(s, an, bal) { }
	virtual ~Brass() { };

	virtual void Withdraw(double amt);
	virtual void ViewAcct() const;
};

// Brass Plus Account Class
class BrassPlus : public AcctABC
{
public:
	BrassPlus(const std::string& s = "Nullbody", long an = -1,
		double bal = 0.0, double ml = 500, double r = 0.10);
	BrassPlus(const Brass& ba, double ml = 500, double r = 0.1);
	virtual void ViewAcct() const;
	virtual void Withdraw(double amt);
	void ResetMax(double m) { maxLoan = m; }
	void ResetRate(double r) { rate = r; }
	void ResetOwes() { owesBank = 0; }

private:
	double maxLoan;
	double rate;
	double owesBank;
};