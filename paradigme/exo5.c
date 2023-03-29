int boh(){
    int n = 7;
    int somme = 0;
    int somme2 = 0;
    for(int k = 0; k<=n; k++){
        somme += 2* k + 1;
    }
    for(int l = 0; l<=n; l++){
        somme2 += 2* l;
    }

    return somme - somme2;
}

int main(int argc, char const *argv[])
{
    int a = boh();
    printf("%d", a);
    return 0;
}
