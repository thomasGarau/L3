// Generated automatically with "cito". Do not edit.
using System;

[Flags]
enum Seasons
{
	Spring = 1,
	Summer = 2,
	Fall = 4,
	Winter = 8,
	Autumn = Fall,
	Warm = Spring | Summer,
	Cold = Fall | Winter
}
