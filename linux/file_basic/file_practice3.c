#include <stdio.h>
#include <string.h>

struct image
{
    char pixel;
    int points;
    char name[20];
};

static int write_to_file(void)
{
    FILE* fp;
    struct image img1 = {
        3, 10, "img1"
    };
    struct image img2 = {
        4, 16, "img2"
    };

    fp = fopen("images", "w");
    if (fp == NULL)
    {
        return -1;
    }

    if (fwrite(&img1, sizeof(struct image), 1, fp) != 1)
    {
        fclose(fp);
        return -1;
    }
    if (fwrite(&img2, sizeof(struct image), 1, fp) != 1)
    {
        fclose(fp);
        return -1;
    }

    fclose(fp);
    return 0;
}

static int read_from_file(void)
{
    FILE* fp;
    int i;
    struct image images[2];

    if (!(fp = fopen("images", "r")))
    {
        return -1;
    }

    if (fread(images, sizeof(struct image), 2, fp) != 2)
    {
        fclose(fp);
        return -1;
    }
    fclose(fp);

    for (i = 0; i < 2; i++)
    {
        printf("pixel: %d, points: %d, name: %s\n", 
            images[i].pixel,
            images[i].points,
            images[i].name
        );
    }

    return 0;
}

int main(int argc, char** argv)
{
    write_to_file();

    read_from_file();
    return 0;
}
