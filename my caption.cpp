#include <stdio.h> 
int main() { 
    printf("Enter the marks of students: "); 
    int marks; 
    scanf("%d", &marks);
if (marks>85 && marks<100)
    {
            printf("GRADE A");
    }
    else if (marks>70 && marks<85)
    {
        printf("GRADE B");
    }
    else if (marks>55 && marks<70)
    {
        printf("GRADE C");
    }
    else if (marks>35 && marks<55)
    {   
        printf("GRADE D");
    }
    else if ( marks<35)
    {
        printf("FAIL");
    }
    
	else 
    {
	printf("Enter the valid marks");
    }
return 0;
}
