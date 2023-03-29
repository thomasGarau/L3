#include <stdio.h>
int main(int argc, char* argv[])
{
    int MonnaieARendre=140;  // 122 en centimes d euros par exemple
    int tableauPieces[6]={1,10,21,34,70,100};  // tableau trie de pieces disponibles
    int tableauPiecesRendues[100]={0};// 100 pieces max par exemple
    int monnaieRendu = 0;
    int len = sizeof(tableauPieces) / sizeof(tableauPieces[0]);
    int i = 0;
    int j = 0;
    int z = 0;
    while(monnaieRendu != MonnaieARendre){
        if (tableauPieces[len - i] + monnaieRendu <= MonnaieARendre){
            tableauPiecesRendues[j] = tableauPieces[len - i];
            monnaieRendu += tableauPieces[len - i];
            j++;
        }else{
            i++;
        }
        z++;
    }
    printf("%d", len);
    for(int a=0; a<j; a++){
       // printf("%d\n", tableauPiecesRendues[a]);
    }

    return 0;
}