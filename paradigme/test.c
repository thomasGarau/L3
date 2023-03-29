typedef struct personne{
    int age; 
    char nom[20];
}Personne;

int main(int argc, char const *argv[])
{
    Personne p;
    Personne* pp;
    pp = &p;
    scanf("%d%s", &p.age, p.nom);
    printf("%d,%s", pp->age, pp->nom);
    return 0;
}
