#include <iostream>
#include <new>

const int BUF = 512;
char buffer[BUF];

struct chaff
{
	char dross[20];
	int slag;
};

int main()
{
	chaff* ptr = new (buffer) chaff[2];
	memcpy(ptr[0].dross, "안녕하세오", 20);
	ptr[0].slag = 3;
	memcpy(ptr[1].dross, "안녕히가세오", 20);
	ptr[1].slag = 5;

	for (int i = 0; i < 2; i++)
	{
		std::cout << "chaff[" << i + 1 << "]의 dross : "
			<< ptr[i].dross << ", slag : " << ptr[i].slag << std::endl;
	}

	return 0;
}