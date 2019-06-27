// dma.h -- ��Ӱ� ���� �޸� ����
#pragma once
#include <iostream>

// DMA�� ����ϴ� ���� Ŭ����
class baseDMA
{
public:
	baseDMA(const char* l = "null", int r = 0);
	baseDMA(const baseDMA& rs);
	virtual ~baseDMA();
	baseDMA& operator=(const baseDMA& rs);

	friend std::ostream& operator<<(std::ostream& os, const baseDMA& rs);

private:
	char* label;
	int rating;
};

// DMA�� ������� �ʴ� �Ļ� Ŭ����
// �ı��ڰ� �ʿ� ����
// �Ͻ��� ���� �����ڸ� ����Ѵ�
// �Ͻ��� ���� �����ڸ� ����Ѵ�
class lacksDMA : public baseDMA
{
public:
	lacksDMA(const char* c = "blank", const char* l = "null", int r = 0);
	lacksDMA(const char* c, const baseDMA& rs);

	friend std::ostream& operator<<(std::ostream& os, const lacksDMA& rs);

private:
	enum { COL_LEN = 40 };
	char color[COL_LEN];
};

// DMA�� ����ϴ� �Ļ� Ŭ����
class hasDMA : public baseDMA
{
public:
	hasDMA(const char* s = "none", const char* l = "null", int r = 0);
	hasDMA(const char* s, const baseDMA& rs);
	hasDMA(const hasDMA& hs);
	~hasDMA();
	hasDMA& operator=(const hasDMA& rs);

	friend std::ostream& operator<<(std::ostream& os, const hasDMA& rs);

private:
	char* style;
};
