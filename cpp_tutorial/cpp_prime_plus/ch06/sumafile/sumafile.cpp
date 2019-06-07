// sumafile.cpp -- �迭 �Ű������� ����ϴ� �Լ�
#include <iostream>
#include <fstream>		// ���� I/O ����
#include <cstdlib>		// exit() ����
const int SIZE = 60;
int main()
{
	using namespace std;
	char filename[SIZE];
	ifstream inFile;			// ���� �Է��� ó���ϱ� ���� �ܰ�
	cout << "������ ������ �̸��� �Է��Ͻÿ�: ";
	cin.getline(filename, SIZE);
	inFile.open(filename);		// inFile�� ���Ͽ� �����Ѵ�
	if (!inFile.is_open())
	{
		cout << filename << " ������ �� �� �����ϴ�." << endl;
		cout << "���α׷��� �����մϴ�.\n";
		exit(EXIT_FAILURE);
	}
	double value;
	double sum = 0.0;
	int count = 0;				// ���� �׸��� ����
	
	inFile >> value;			// ù ��° ���� ��´�
	while (inFile.good())		// �Է��� ��ȣ�ϰ� EOF�� �ƴ� ����
	{
		++count;				// �׸� ���� �ϳ� �߰�
		sum += value;			// ���踦 ����Ѵ�
		inFile >> value;		// ���� ���� ��´�
	}
	if (inFile.eof())
		cout << "���� ���� �����߽��ϴ�.\n";
	else if (inFile.fail())
		cout << "������ ����ġ�� �Է��� ����Ǿ����ϴ�.\n";
	else
		cout << "�� �� ���� ������ �Է��� ����Ǿ����ϴ�.\n";

	if (count == 0)
		cout << "�����Ͱ� �����ϴ�.\n";
	else
	{
		cout << "���� �׸��� ����: " << count << endl;
		cout << "�հ�: " << sum << endl;
		cout << "���: " << sum / count << endl;
	}
	inFile.close();				// ���� ó�� ����
	return 0;
}