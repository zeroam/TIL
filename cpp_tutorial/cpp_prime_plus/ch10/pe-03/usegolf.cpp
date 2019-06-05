#include "golf.h"

int main()
{
	Golf ann("Ann Birdfree", 24);
	ann.ShowGolf();

	ann.SetGolf();
	ann.ShowGolf();

	ann.Handicap(20);
	ann.ShowGolf();

	return 0;
}