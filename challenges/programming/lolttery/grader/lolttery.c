#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <time.h>
#include <unistd.h>


void print_banner()
{
    puts(" __      ______  __      ______  ______  ______  ______  __  __    ");
    puts("/\\ \\    /\\  __ \\/\\ \\    /\\__  _\\/\\__  _\\/\\  ___\\/\\  == \\/\\ \\_\\ \\   ");
    puts("\\ \\ \\___\\ \\ \\/\\ \\ \\ \\___\\/_/\\ \\/\\/_/\\ \\/\\ \\  ___\\ \\  __<\\ \\____ \\  ");
    puts(" \\ \\_____\\ \\_____\\ \\_____\\ \\ \\_\\   \\ \\_\\ \\ \\_____\\ \\_\\ \\_\\/\\_____\\ ");
    puts("  \\/_____/\\/_____/\\/_____/  \\/_/    \\/_/  \\/_____/\\/_/ /_/\\/_____/ ");
}

void handler(int sig)
{
    puts("\nYOU'RE SO SLOW THAT WE GAVE YOUR TICKETS AWAY!");

    exit(0);
}

int main()
{
    srand(time(NULL));

    int secret = rand() % 1000000 + 1;
    char guess[9];

    print_banner();

    puts("**************************************************************************************");
    puts("|              1 to 1000000, 20 LOTTERY TICKETS. CAN YOU DO IT??                     |");
    puts("**************************************************************************************");
    fflush(stdout);

    signal(SIGALRM, handler);

    for(int i = 0; i < 20; i++) {
        printf("TICKET #%02d => ", i+1);
        fflush(stdout);
        alarm(2);
        fgets(guess, sizeof(guess), stdin);

        if (atoi(guess) == secret) {
            puts("flag{Y0u_4r3_RNG_G0d}");
            fflush(stdout);
            exit(0);
        } else if(atoi(guess) > secret) {
            puts("THE MYSTICAL COW SAYS: TOO HIGH");
            fflush(stdout);
        } else {
            puts("THE MYSTICAL COW SAYS: TOO LOW");
            fflush(stdout);
        }
    }
    puts("\nYOU RAN OUT OF TICKETS. SPENT ALL YOUR MONEY. YOU ARE BROKE. HAVE A NICE LIFE!");
    fflush(stdout);

    return 0;
}
