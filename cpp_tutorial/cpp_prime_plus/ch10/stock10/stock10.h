// stock10.h -- �����ڵ�� �ı��ڰ� �߰��� Stock Ŭ���� ����
#pragma once

#include <string>

class Stock
{
private:
	std::string company;
	long shares;
	double share_val;
	double total_val;
	void set_tot() { total_val = shares * share_val; }

public:
	// �ΰ��� ������
	Stock();			// ������ ������
	Stock(const std::string& co, long n = 0, double pr = 0.0);
	~Stock();			// �ı���
	void buy(long num, double price);
	void sell(long num, double price);
	void update(double price);
	void show();
};

