#include <iostream>
#include <array>
#include <vector>

int main()
{
	// 01
	char actors[30];
	short betsie[100];
	float chuck[13];
	long double dipsea[64];

	// 02
	std::array<char, 30> actors2;
	std::array<short, 100> betsie2;
	std::array<float, 13> chuck2;
	std::array<long double, 64> dipsea2;

	// 03
	int arr[5] = { 1, 3, 5, 7, 9 };

	// 04
	int even = arr[0] + arr[4];

	// 05
	float ideas[3] = { 0.1, 0.2, 0.3 };
	std::cout << "ideas[2]: " << ideas[2] << std::endl;

	// 06
	char cb[] = "cheeseburger";

	// 07
	std::string ws = "Waldorf Salad";

	// 08
	struct fish
	{
		char kind[20];
		int weight;
		float length;
	};

	// 09
	fish piranna = { "piranna", 10, 100 };

	// 10
	enum Response
	{
		No,
		Yes,
		Maybe
	};

	// 11
	double ted = 1.23456;
	double* pted = &ted;
	std::cout << "ted: " << *pted << std::endl;

	// 12
	float treacle[10] = { 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0 };
	float* ptreacle = treacle;
	std::cout << "treacle fist, last element: " << *ptreacle << ", " << *(ptreacle + sizeof(treacle) / sizeof(float) - 1) << std::endl;
	std::cout << "treacle fist, last element: " << ptreacle[0] << ", " << ptreacle[9] << std::endl;

	// 13
	unsigned int num;
	std::cout << "양의 정수를 하나 입력하시오: ";
	std::cin >> num;
	int* pnums = new int[num];
	std::vector<int> num_vec(num);
	delete[] pnums;

	// 14
	std::cout << (int*) "Home of the jolly bytes" << std::endl;

	// 15
	fish* dy_fish = new fish;
	std::cout << "물고기 종류를 입력하시오: ";
	std::cin >> dy_fish->kind; 

	// 16
	const int size = 10;
	std::vector<std::string> str_vector(size);
	std::array<std::string, size> str_array;

	return 0;
}