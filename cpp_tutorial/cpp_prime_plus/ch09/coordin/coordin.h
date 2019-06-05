#pragma once
// coordin.h -- ����ü ���ø��� �Լ� ����
// ����ü ���ø�
#ifndef COORDIN_H_
#define COORDIN_H_

struct polar
{
	double distance;		// �������κ����� �Ÿ�
	double angle;			// ���������κ����� ����
};

struct rect
{
	double x;				// �������κ����� ���� �Ÿ�
	double y;				// �������κ����� ���� �Ÿ�
};

// ����
polar rect_to_polar(rect xypos);
void show_polar(polar dapos);

#endif