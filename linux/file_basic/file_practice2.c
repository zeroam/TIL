#include <stdio.h>
#include <string.h>

int read_from_file(void)
{
    FILE* fp;
    char buf[1024];
    
    fp = fopen("data", "r");

    if (fp == NULL)
    {
        perror("fopen error\n");
        return -1;
    }

    memset(buf, 0, sizeof(buf));
    while (fgets(buf, sizeof(buf), fp) != NULL)
    {
        printf("%s", buf);
    }
    fclose(fp);


    return 0;
}

int main(int argc, char** argv)
{
    read_from_file();
    return 0;
}
