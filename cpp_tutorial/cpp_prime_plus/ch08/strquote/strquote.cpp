// strquote.cpp -- ���� �ٸ� ����
#include <iostream>
#include <string>
using namespace std;
string version1(const string& s1, const string& s2);
const string& version2(string& s1, const string& s2);	// �μ� ȿ��
const string& version3(string& s1, const string& s2);	// ���� ����
int main()
{
	string input;
	string copy;
	string result;

	cout << "���ڿ��� �Է��Ͻÿ�: ";
	getline(cin, input);
	copy = input;
	cout << "�Է��� ���ڿ�: " << input << endl;
	result = version1(input, "***");
	cout << "�ٲ� ���ڿ�: " << result << endl;
	cout << "���� ���ڿ�: " << input << endl;

	result = version2(input, "###");
	cout << "�ٲ� ���ڿ�: " << result << endl;
	cout << "���� ���ڿ�: " << input << endl;
	
	cout << "���� ���ڿ� �缳��\n";
	input = copy;
	result = version3(input, "@@@");
	cout << "�ٲ� ���ڿ�: " << result << endl;
	cout << "���� ���ڿ�: " << input << endl;

	return 0;
}

string version1(const string& s1, const string& s2)
{
	string temp;

	temp = s2 + s1 + s2;
	return temp;
}

const string& version2(string& s1, const string& s2)	// �μ� ȿ��
{
	s1 = s2 + s1 + s2;
	// �Լ��� ���޵� ������ �����ϹǷ� �����ϴ�
	return s1;
}

const string& version3(string& s1, const string& s2)	// ���� ����
{
	string temp;

	temp = s2 + s1 + s2;
	// ���� ������ ���� ������ �����ϹǷ� �������� �ʴ�
	return temp;
}