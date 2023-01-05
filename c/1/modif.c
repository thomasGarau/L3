#include <stdio.h>


typedef struct coord{
    int x, y;
}Coord;

void modif(Coord *pt){
    pt->x ++;
    if (pt->x > 1000){
        pt->x = 0;
    }
}


int main(int argc, char const *argv[])
{
  Coord p1 = {1, 2};
  Coord *pt_cord = &p1;
  modif(pt_cord);
  printf("%d", pt_cord->x);
}
