#include "03.h"
#include <iostream>
#include <iomanip>

namespace num3
{
	void program()
	{
		box box1 = { "Rasberrypi", 10, 20, 30, 40 };

		box_print(box1);
		box_set_volume(&box1);
		box_print(box1);

		std::cout << "프로그램을 종료합니다.\n";
	}

	void box_print(box box)
	{
		using std::cout;
		using std::endl;
		using std::setw;
		using std::left;

		cout << left;
		cout << "box 구조체 출력\n";
		cout << setw(10) << "  maker: " << box.maker << endl;
		cout << setw(10) << "  height: " << box.height << endl;
		cout << setw(10) << "  width: " << box.width << endl;
		cout << setw(10) << "  length: " << box.length << endl;
		cout << setw(10) << "  volume: " << box.volume << endl;

	}

	void box_set_volume(box* pbox)
	{
		using std::cout;

		cout << "box 구조체 volume 설정\n";
		pbox->volume = pbox->height * pbox->width * pbox->length;
	}
}