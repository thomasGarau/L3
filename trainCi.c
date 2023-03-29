/* Generated automatically with "cito". Do not edit.*/
#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include "trainCi.h"

static char *CiString_Format(const char *format, ...)
{
	va_list args1;
	va_start(args1, format);
	va_list args2;
	va_copy(args2, args1);
	size_t len = vsnprintf(NULL, 0, format, args1) + 1;
	va_end(args1);
	char *str = malloc(len);
	vsnprintf(str, len, format, args2);
	va_end(args2);
	return str;
}

typedef void (*CiMethodPtr)(void *);
typedef struct {
	size_t count;
	size_t unitSize;
	size_t refCount;
	CiMethodPtr destructor;
} CiShared;

static void *CiShared_Make(size_t count, size_t unitSize, CiMethodPtr constructor, CiMethodPtr destructor)
{
	CiShared *self = (CiShared *) malloc(sizeof(CiShared) + count * unitSize);
	self->count = count;
	self->unitSize = unitSize;
	self->refCount = 1;
	self->destructor = destructor;
	if (constructor != NULL) {
		for (size_t i = 0; i < count; i++)
			constructor((char *) (self + 1) + i * unitSize);
	}
	return self + 1;
}

static void CiShared_Release(void *ptr)
{
	if (ptr == NULL)
		return;
	CiShared *self = (CiShared *) ptr - 1;
	if (--self->refCount != 0)
		return;
	if (self->destructor != NULL) {
		for (size_t i = self->count; i > 0;)
			self->destructor((char *) ptr + --i * self->unitSize);
	}
	free(self);
}

struct Main {
};

struct Train {
	const char *villeDepart;
	const char *villeArrive;
	const Horaire *temps;
	int distance;
};
static void Train_Construct(Train *self);

struct Horaire {
	const char *depart;
	const char *arrive;
	const Gare *gare;
};
static void Horaire_Construct(Horaire *self);

struct Gare {
	struct Train *listTrain;
	struct Horaire *listHoraire;
};
static void Gare_Construct(Gare *self);
static void Gare_Destruct(Gare *self);

void Main_main(const char *const *args)
{
	Gare *maGare = (Gare *) CiShared_Make(1, sizeof(Gare), (CiMethodPtr) Gare_Construct, (CiMethodPtr) Gare_Destruct);
	Horaire *h1 = (Horaire *) CiShared_Make(1, sizeof(Horaire), (CiMethodPtr) Horaire_Construct, NULL);
	Horaire_init(h1, 8, 0, 8, 59, maGare);
	CiShared_Release(h1);
	CiShared_Release(maGare);
}

static void Train_Construct(Train *self)
{
}

Train *Train_New(void)
{
	Train *self = (Train *) malloc(sizeof(Train));
	if (self != NULL)
		Train_Construct(self);
	return self;
}

void Train_Delete(Train *self)
{
	free(self);
}

void Train_init(Train *self, const char *nVilleDepart, const char *nVilleArrive, const Horaire *nTabHoraire, int nDistance)
{
	self->distance = nDistance;
	self->villeArrive = nVilleArrive;
	self->villeDepart = nVilleDepart;
	self->temps = nTabHoraire;
}

static void Horaire_Construct(Horaire *self)
{
}

Horaire *Horaire_New(void)
{
	Horaire *self = (Horaire *) malloc(sizeof(Horaire));
	if (self != NULL)
		Horaire_Construct(self);
	return self;
}

void Horaire_Delete(Horaire *self)
{
	free(self);
}

void Horaire_init(Horaire *self, int nHeureDepart, int nMinuteDepart, int nHeureArrive, int nMinuteArrive, const Gare *nGare)
{
	if (nHeureArrive < 10 && nMinuteArrive < 10) {
		self->arrive = CiString_Format("0%d:0%d", nHeureArrive, nMinuteArrive);
	}
	else if (nHeureArrive < 10) {
		self->arrive = CiString_Format("0%d:%d", nHeureArrive, nMinuteArrive);
	}
	else if (nMinuteArrive < 10) {
		self->arrive = CiString_Format("%d:0%d", nHeureArrive, nMinuteArrive);
	}
	else {
		self->arrive = CiString_Format("%d:0%d", nHeureArrive, nMinuteArrive);
	}
	if (nHeureDepart < 10 && nMinuteDepart < 10) {
		self->depart = CiString_Format("0%d:0%d", nHeureDepart, nMinuteDepart);
	}
	else if (nMinuteDepart < 10) {
		self->depart = CiString_Format("%d:0%d", nHeureDepart, nMinuteDepart);
	}
	else if (nHeureArrive < 10) {
		self->depart = CiString_Format("0%d:%d", nHeureDepart, nMinuteDepart);
	}
	else {
		self->depart = CiString_Format("%d:%d", nHeureDepart, nMinuteDepart);
	}
	self->gare = nGare;
	Gare_setListHoraire(self->gare, self);
}

static void Gare_Construct(Gare *self)
{
	self->listTrain = malloc(100*sizeof(Train));
	self->listHoraire =  malloc(100*sizeof(Train));
}

static void Gare_Destruct(Gare *self)
{
	free(self->listHoraire);
	free(self->listTrain);
}

Gare *Gare_New(void)
{
	Gare *self = (Gare *) malloc(sizeof(Gare));
	if (self != NULL)
		Gare_Construct(self);
	return self;
}

void Gare_Delete(Gare *self)
{
	if (self == NULL)
		return;
	Gare_Destruct(self);
	free(self);
}

void Gare_setListHoraire(const Gare *self, const Horaire *h)
{
	const Horaire *citemp0 = h;
	g_array_append_val(self->listHoraire, citemp0);
}
