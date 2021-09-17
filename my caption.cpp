#include <stdio.h> 
int main() 
{ 
    printf("Enter the marks of students: "); 
    int marks; 
    scanf("%d", &marks);
if (marks>85 && marks<100)
    {
            printf("GRADE A");
    }
    else if (marks>70 && marks<84)
    {
        printf("GRADE B");
    }
    else if (marks>55 && marks<69)
    {
        printf("GRADE C");
    }
    else if (marks>40 && marks<54)
    {   
        printf("GRADE D");
    }
    else if ( marks<40)
    {
        printf("GRADE F");
    }
    
	else 
    {
	printf("Enter the valid marks");
    }
return 0;
}
