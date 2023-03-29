int main(int argc, char const *argv[])
{
    int c = soustraction(55,50);
    int d = complement(17,13);
    printf("%d%d", c,d);
    return 0;
}

int soustraction(int a, int b){
    return a^b;
}

int complement(int a, int b){
    return ~a + b +1;
}