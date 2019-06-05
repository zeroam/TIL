// arrfun2.cpp -- 배열 매개변수를 사용하는 함수
#include <iostream>
const int ArSize = 8;
int sum_arr(int arr[], int n);

int main()
{
	int cookies[ArSize] = { 1, 2, 4, 8, 16, 32, 64, 128 };

	std::cout << cookies << " = 배열 주소, ";

	std::cout << "sizeof cookies = " << sizeof cookies << std::endl;
	int sum = sum_arr(cookies, ArSize);
	std::cout << "먹은 과자 수 합계: " << sum << std::endl;
	sum = sum_arr(cookies, 3);			// 배열 원소 개수 속이기
	std::cout << "처음 세 사람은 과자 " << sum << "개를 먹었습니다.\n";
	sum = sum_arr(cookies + 4, 4);		// 배열 원소 개수 속이기
	std::cout << "마지막 네 사람은 과자 " << sum << "개를 먹었습니다.\n";
	return 0;
}

// 정수 배열의 합계를 리턴한다
int sum_arr(int arr[], int n)
{
	int total = 0;
	std::cout << arr << " = arr, ";
	std::cout << "sizeof arr = " << sizeof arr << std::endl;
	for (int i = 0; i < n; i++)
		total = total + arr[i];
	return total;
}