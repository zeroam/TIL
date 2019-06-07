// stone.cpp -- ����� ���� �������� ��ȯ
#include <iostream>
#include "stonewt.h"

using std::cout;

void display(const Stonewt& st, int n);

int main()
{
	Stonewt pavarotti = 275;		// �����ڸ� ����Ͽ� �ʱ�ȭ �Ѵ�
	Stonewt wolfe(285.7);			// Stonewt wolfe = 285.7;�� ����
	Stonewt taft(21, 8);

	cout << "�׳� ������ ������: ";
	pavarotti.show_stn();
	cout << "Ž���� ������: ";
	wolfe.show_stn();
	cout << "������� ������: ";
	taft.show_lbs();
	pavarotti = 276.8;				// ��ȯ�� ���� �����ڸ� ����Ѵ�
	taft = 325;						// taft = Stonewt(325);�� ����
	cout << "���� �Ļ縦 ��ģ �� �׳� ������ ������: ";
	pavarotti.show_stn();
	cout << "���� �Ļ縦 ��ģ �� ������� ������: ";
	taft.show_lbs();
	display(taft, 2);
	cout << "������ ������ �׺��� �� ���̴�.\n";
	display(422, 2);				// �Ű������� int�� ���� -> double �ڵ��� ��ȯ, �����ڸ� ȣ���Ͽ� �ӽð�ü ����
	cout << "���� �ǰ��� �ִ��� ���̴�.\n";

	return 0;
}

void display(const Stonewt& st, int n)
{
	for (int i = 0; i < n; i++)
	{
		cout << "��! ";
		st.show_stn();
	}
}