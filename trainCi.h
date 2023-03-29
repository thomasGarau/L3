// Generated automatically with "cito". Do not edit.
#pragma once
#ifdef __cplusplus
extern "C" {
#endif
typedef struct Main Main;
typedef struct Train Train;
typedef struct Horaire Horaire;
typedef struct Gare Gare;

void Main_main(const char *const *args);

Train *Train_New(void);
void Train_Delete(Train *self);

void Train_init(const Train *self, const char *nVilleDepart, const char *nVilleArrive, const Horaire *nTabHoraire, int nDistance);

Horaire *Horaire_New(void);
void Horaire_Delete(Horaire *self);

void Horaire_init(const Horaire *self, int nHeureDepart, int nMinuteDepart, int nHeureArrive, int nMinuteArrive, const Gare *nGare);

Gare *Gare_New(void);
void Gare_Delete(Gare *self);

void Gare_setListHoraire(const Gare *self, const Horaire *h);

#ifdef __cplusplus
}
#endif
