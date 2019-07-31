#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

void test_func(void)
{
    printf("this is test function(pid %d)\n", getpid());
}

int main(int argc, char** argv)
{
    pid_t pid;
    int exit_status;

    printf("origin process pid: %d\n", getpid());

    pid = fork();
    if (pid == 0)
    {
        /* child process */
        printf("child process pid: %d\n", getpid());
        if (execl("/bin/ls", "ls", "-al", "/tmp", NULL) == -1)
        {
            printf("exec() fail\n");
            return -1;
        }
    }
    else if (pid > 0)
    {
        /* parent process */
        printf("parent process pid: %d, child pid %d\n", getpid(), pid);
    }
    test_func();

    pid = wait(&exit_status);
    if (WIFEXITED(exit_status))
    {
        printf("child %d returns %d\n",
                pid, WEXITSTATUS(exit_status));
    } else
    {
        printf("child %d is not exited\n", pid);
    }

    return 0;
}
