// outfile.cpp -- ���Ͽ� ����
#include <iostream>
#include <fstream>		// ���� I/O�� ����
int main()
{
	using namespace std;

	char automobile[50];
	int year;
	double a_price;
	double d_price;

	ofstream outFile;				// ����� ���� ��ü ����
	outFile.open("carinfo.txt");	// ���Ͽ� ����

	cout << "�ڵ��� ����Ŀ�� ������ �Է��Ͻÿ�: ";
	cin.getline(automobile, 50);
	cout << "������ �Է��Ͻÿ�: ";
	cin >> year;
	cout << "���� ������ �Է��Ͻÿ�: ";
	cin >> a_price;
	d_price = 0.913 * a_price;

	// cout���� ��ũ���� ������ ���÷���
	cout << fixed << showpoint;
	cout.precision(2);
	cout << "����Ŀ�� ����: " << automobile << endl;
	cout << "����: " << year << endl;
	cout << "���԰��� $" << a_price << endl;
	cout << "���簡�� $" << d_price << endl;

	// cout ��� outFile�� ����Ͽ� �Ȱ��� ���� ó���� �� �ִ�
	outFile << fixed << showpoint;
	outFile.precision(2);
	outFile << "����Ŀ�� ����: " << automobile << endl;
	outFile << "����: " << year << endl;
	outFile << "���԰��� $" << a_price << endl;
	outFile << "���簡�� $" << d_price << endl;

	outFile.close();		// ���� ó�� ����
	return 0;

}