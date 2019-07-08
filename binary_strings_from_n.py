void binary(int n)
{
    if(n < 1)
        printf("%s\n",A);    // Assume A is a global variable
    else
    {
        A[n-1] = '0';
        binary(n-1);
        A[n-1] = '1';
        binary(n-1);
    }
}
