#pragma once

const int Len = 40;
struct golf
{
	char fullname[Len];
	int handicap;
};

// ���ȭ�� ����:
// �� �Լ��� ���������� ���޵� ������ ����Ͽ�
// golf ����ü�� ������ �̸��� �ڵ�ĸ���� �����Ѵ�
void setgolf(golf& g, const char* name, int hc);

// ��ȭ�� ����:
// �� �Լ��� ����ڿ��� �̸��� �ڵ�ĸ�� ���´�
// g�� ������� �Էµ� ������ �����Ѵ�
// �̸��� �ԷµǸ� 1�� �����ϰ�, �̸��� �� ���ڿ��̸� 0�� �����Ѵ�
int setgolf(golf& g);

// �� �Լ��� handicap�� ���ο� ������ �����Ѵ�
void handicap(golf& g, int hc);

// �� �Լ��� golf ����ü�� ������ ����Ѵ�
void showgolf(const golf& g);
