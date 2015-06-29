
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char rot13_char(char c) {
    if (isalpha(c)) {
        char alpha = islower(c) ? 'a' : 'A';
        return (c - alpha + 13) % 26 + alpha;
    }
    return c;
}

int main(int argc, char * argv[] ) {

FILE * input; //Input File
FILE * output;
char iChar;
char nowChar;
char extraChar;

input=fopen(argv[1], "r");
output=fopen(argv[2],"w");

if (input == NULL || output == NULL) {
	printf("Usage: ./shitrot <input file> <output file>\n");
	return 1;
}

int i = 0;
do{
	iChar = fgetc(input);
	if(iChar!=EOF){
		if(isalpha(iChar)){
			nowChar =rot13_char(iChar);
			fputc(nowChar,output);
			extraChar = 97 + ((i+iChar)%26);
			fputc(extraChar,output);
			i++;
		}
	}

}while(iChar != EOF);

fclose(input);
fclose(output);

}
