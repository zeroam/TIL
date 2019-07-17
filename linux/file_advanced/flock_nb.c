#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/file.h>
#include <errno.h>

static void print_usage(const char* progname)
{
    printf("usage: %s (ex|sh)\n", progname);
    exit(-1);
}

int main(int argc, char** argv)
{
    int fd;
    int ops;

    if (argc < 2)
    {
        print_usage(argv[0]);
    }

    if (!strcmp(argv[1], "sh"))
    {
        ops = LOCK_SH;
    }
    else if (!strcmp(argv[1], "ex"))
    {
        ops = LOCK_EX;
    }
    else
    {
        print_usage(argv[0]);

    }

    fd = open("lockfile", O_RDWR | O_CREAT, 0644);
    if (fd < 0)
    {
        printf("open() fail\n");
        return -1;
    }

    printf("trying to grab the lock\n");
    if (flock(fd, ops | LOCK_NB) != 0)
    {
        printf("flock(ops %d), errno=%d(%s)\n", ops, errno, strerror(errno));
        close(fd);
        return -1;
    }
    printf("grab the lock!!\n");
    getc(stdin);

    if (flock(fd, LOCK_UN))
    {
        printf("floack(unlock)\n");
        close(fd);
        return -1;
    }

    close(fd);
    return 0;
}
