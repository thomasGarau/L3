#include <stdio.h>
void complexite(int n){
    int x =0;
    int y =0;

    for(int k=1; k<n; k*=2){
        x += 1;
        for(int j=0;j<n;j++){
            y += 1;
        }
    }
    printf("%d", x+y);
}

int main(int argc, char const *argv[])
{
complexite(10);
return 0;
}
 