#pragma once

namespace num3
{
	struct box
	{
		char maker[40];
		float height;
		float width;
		float length;
		float volume;
	};

	void program();
	void box_print(box box);
	void box_set_volume(box* pbox);
}
