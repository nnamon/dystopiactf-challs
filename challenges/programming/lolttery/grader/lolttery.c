#include <stdio.h>
#include <stdlib.h>
#include <time.h>


void print_banner()
{
    puts(" __      ______  __      ______  ______  ______  ______  __  __    ");
    puts("/\\ \\    /\\  __ \\/\\ \\    /\\__  _\\/\\__  _\\/\\  ___\\/\\  == \\/\\ \\_\\ \\   ");
    puts("\\ \\ \\___\\ \\ \\/\\ \\ \\ \\___\\/_/\\ \\/\\/_/\\ \\/\\ \\  ___\\ \\  __<\\ \\____ \\  ");
    puts(" \\ \\_____\\ \\_____\\ \\_____\\ \\ \\_\\   \\ \\_\\ \\ \\_____\\ \\_\\ \\_\\/\\_____\\ ");
    puts("  \\/_____/\\/_____/\\/_____/  \\/_/    \\/_/  \\/_____/\\/_/ /_/\\/_____/ ");
}
int main()
{
    srand(time(NULL));

    int secret = rand() % 1000000 + 1;
    char * guess;

    print_banner();

    puts("**************************************************************************************");
    puts("|              1 to 1000000, 20 LOTTERY TICKETS. CAN YOU DO IT??                     |");
    puts("**************************************************************************************");
    fflush(stdout);

    for(int i = 0; i < 20; i++) {
        printf("TICKET #%02d => ", i+1);
        fflush(stdout);
        scanf("%s", guess);

        if (atoi(guess) == secret) {
            puts("flag{Y0u_4r3_RNG_G0d}");
            exit(0);
        } else if(atoi(guess) > secret) {
            puts("THE MYSTICAL COW SAYS: TOO HIGH");
        } else {
            puts("THE MYSTICAL COW SAYS: TOO LOW");
        }
    }
    puts("\nYOU RAN OUT OF TICKETS. SPENT ALL YOUR MONEY. YOU ARE BROKE. HAVE A NICE LIFE!");
    fflush(stdout);

    return 0;
}
