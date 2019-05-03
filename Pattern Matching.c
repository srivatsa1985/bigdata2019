#include <stdio.h>
#include <string.h>

#define LEN 20

int lookup[LEN][LEN];

int match(char str[], char pattern[], int n, int m)
{

	if (m < 0 && n < 0)
		return 1;

	else if (m < 0)
		return 0;


	else if (n < 0)
	{
		for (int i = 0; i <= m; i++)
			if (pattern[i] != '*')
				return 0;

		return 1;
	}


	if (lookup[m][n] == -1)
	{
		if (pattern[m] == '*')
		{


			lookup[m][n] = match(str, pattern, n - 1, m) ||
						match(str, pattern, n, m - 1);
		}
		else
		{

			if (pattern[m] != '.' && pattern[m] != str[n])
				lookup[m][n] = 0;

			else
				lookup[m][n] = match(str, pattern, n - 1, m - 1);
		}
	}

	return lookup[m][n];
}

int main(void)
{

	char str[20];
	char pattern[20];

	printf("Enter 1st sequence:");
	scanf("%s",str);
	printf("Enter 2nd sequence:");
	scanf("%s",pattern);
	printf("\nSolution is ");

	memset(lookup, -1, sizeof(lookup));

	if (match(str, pattern, strlen(str) - 1, strlen(pattern) - 1))
		printf("TRUE");
	else
		printf("FALSE");

	return 0;
}
