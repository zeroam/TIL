#include <stdio.h>
#include <string.h>

int write_to_file(int argc, char** argv)
{
    FILE* fp;
    fp = fopen("data", "w");

    if (fp == NULL)
    {
        perror("fopen error\n");
        return -1;
    }

    int i;
    for (i = 1; i < argc; i++)
    {
        fputs(argv[i], fp);
        fputs("\n", fp);
    }

    fclose(fp);
    return 0;
}

int main(int argc, char** argv)
{
    int i;
    printf("argc: %d\n", argc);

    for (i = 1; i < argc; i++)
    {
        printf("argv: %s\n", argv[i]);
    }

    if (argc > 1)
    {
        int result = write_to_file(argc, argv);
        if (result)
        {
            printf("write error\n");
            return -1;
        }
    }
    return 0;
}
