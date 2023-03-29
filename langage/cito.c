// Generated automatically with "cito". Do not edit.
#include <stdlib.h>
#include "cito.h"

typedef enum {
	Seasons_SPRING = 1,
	Seasons_SUMMER = 2,
	Seasons_FALL = 4,
	Seasons_WINTER = 8,
	Seasons_AUTUMN = Seasons_FALL,
	Seasons_WARM = Seasons_SPRING | Seasons_SUMMER,
	Seasons_COLD = Seasons_FALL | Seasons_WINTER
} Seasons;
