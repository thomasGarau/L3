// Generated automatically with "cito". Do not edit.
#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include "test6.h"

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

struct TestString {
};

int main(int argc, char const *argv[])
{
	const char *name = "Jhon";
	int born = 1979;
	int now = 2019;
	char *s = CiString_Format("%s is %d years old ", name, now - born);
	puts(s);
	free(s);
	return 0;
}

