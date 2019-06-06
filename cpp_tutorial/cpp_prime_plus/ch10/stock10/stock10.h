// stock10.h -- 생성자들과 파괴자가 추가된 Stock 클래스 선언
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
	// 두개의 생성자
	Stock();			// 디폴츠 생성자
	Stock(const std::string& co, long n = 0, double pr = 0.0);
	~Stock();			// 파괴자
	void buy(long num, double price);
	void sell(long num, double price);
	void update(double price);
	void show();
};

