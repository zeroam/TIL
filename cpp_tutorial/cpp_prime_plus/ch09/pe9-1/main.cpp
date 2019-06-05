#include "golf.h"

int main()
{
	golf ann;
	setgolf(ann, "Ann Birdfree", 24);
	showgolf(ann);

	setgolf(ann);
	showgolf(ann);

	handicap(ann, 20);
	showgolf(ann);

	return 0;
}