// Generated automatically with "cito". Do not edit.
#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include "test4.h"

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
	const char *name;
	int born;
	int now;
	char *s;
};
static void TestString_Construct(TestString *self);
static void TestString_Destruct(TestString *self);

static void TestString_Construct(TestString *self)
{
	self->name = "Jhon";
	self->born = 1979;
	self->now = 2019;
	self->s = CiString_Format("%s is %d years old ", self->name, self->now - self->born);
}

static void TestString_Destruct(TestString *self)
{
	free(self->s);
}

void TestString_Main(const char *const *args)
{
	puts(self->s);
}
