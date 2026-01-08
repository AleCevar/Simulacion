#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    srand(time(NULL));
    FILE * file = fopen("Muestras/muestra_c_4.txt","w");
//    FILE * file2 = fopen("Muestras/muestra_c_8.txt","w");
    for(int i=0; i<1e6; i++) {
        fprintf(file, "%d\n", rand() % 4 + 1);
//        fprintf(file2, "%d\n", rand() % 8 + 1);
    }
    fclose(file);
//    fclose(file2);
    return 0;
}