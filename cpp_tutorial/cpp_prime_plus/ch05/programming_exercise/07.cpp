#include "07.h"
#include <iostream>

void num7::program()
{
	using namespace std;

	int num;

	cout << "�� ���� ���� ������� �����Ͻðڽ��ϱ�? ";
	cin >> num;
	
	// �������� ����ü �迭 ����
	car* cars = new car[num];
	//car** cars = new car*[num];

	for (int i = 0; i < num; i++)
	{
		cout << "�ڵ��� #" << i + 1 << ":\n";
		cout << "���۾�ü : ";
		cin >> cars[i].company;
		//cin >> cars[i]->company;
		cout << "���۳⵵ : ";
		cin >> cars[i].year;
	}

	cout << "���� ���ϰ� �����ϰ� �ִ� �ڵ��� ����� ������ �����ϴ�." << endl;
	for (int i = 0; i < num; i++)
	{
		cout << cars[i].year << "���� " << cars[i].company << endl;
	}
}
