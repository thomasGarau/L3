// Generated automatically with "cito". Do not edit.

interface Seasons
{
	int SPRING = 1;
	int SUMMER = 2;
	int FALL = 4;
	int Winter = 8;
	int AUTUMN = FALL;
	Seasons WARM = SPRING | SUMMER;
	int COLD = FALL | Winter;
}
