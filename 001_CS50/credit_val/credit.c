/*  -
    - credit.c
    -
    - Mark T
    -
    - To validate credit card numbers
    -
    -   */

#include <stdio.h>
//#include <stdlib.h>
//#include <string.h>
//#include <cs50.h>

int validateCard(long long cardNum);
long long GetLongLong(void);

int main(void)
{
    long long cardNum;

    printf("Number: ");
    scanf("%lld", &cardNum);
    
    int result = validateCard(cardNum);
    
    switch (result)
    {
        case 0: // invalid card
        printf("INVALID\n");
        break;
        
        case 1: // valid AMEX
        printf("AMEX\n");
        break;
        
        case 2: // valid MasterCard
        printf("MASTERCARD\n");
        break;
        
        case 3: // valid Visa
        printf("VISA\n");
    }
    
    return 0;
}

int validateCard(long long cardNum) 
{

    int i = 0;
    
    int str[17];
    
    long long a = cardNum;
    while (a >= 10)
    {
        a = a / 10;
        i++;
    }
    
    int length = i + 1;
    
    while(i >= 0)
    {
        str[i] = cardNum % 10;
        cardNum = cardNum / 10;
        i--;
    }
    
    int checkSum = 0;
    int product = 0;
    
    for (i = length - 2; i >= 0; i-=2)
    {
        product = str[i] * 2;
        if (product > 9)
        {
            checkSum += ((product % 10) + 1);
        }
        else 
        {
            checkSum += product;
        }
    }
    
    if (i == -1) 
    {
        i++;
    }
    else if (i == -2)
    {
        i+=3;
    }
    
    int digit = 0;
    
    for (int j = i; j <= length; j+=2)
    {
        digit = str[j];
        checkSum += digit;
    }
    
    if (checkSum % 10 != 0)
    {
        return 0;
    }
    
    if (str[0] == 3 && (str[1] == 4 || str[1] == 7))
    {
        // card is AMEX
        if (length == 15)
        {
            // valid AMEX length
            return 1;
        }
        else return 0;
    }
    else if (str[0] == 5 && (str[1] > 0 && str[1] < 6))
    {
        // card is MasterCard
        if (length == 16)
        {
            // valid MasterCard length
            return 2;
        }
        else return 0;
    }
    else if (str[0] == 4)
    {
        // card is Visa
        if (length == 13 || length == 16)
        {
            // valid Visa length
            return 3;
        }
        else return 0;
    }
    else return 0;
    
}




