// Generated automatically with "cito". Do not edit.
#include <glib.h>
#include <stdio.h>
#include <stdlib.h>
#include "test8.h"

struct TestString {
};

void TestString_Main(const char *const *args)
{
	GArray *tenzeros = g_array_new(FALSE, FALSE, sizeof(int));
	for (int i = 0; i < 10; i++) {
		int citemp0 = 0;
		g_array_append_val(tenzeros, citemp0);
	}
	for (int const *e = (int const *) tenzeros->data, *ciend = e + tenzeros->len; e < ciend; e++) {
		printf("%d\n", *e);
	}
	g_array_free(tenzeros, TRUE);
}
