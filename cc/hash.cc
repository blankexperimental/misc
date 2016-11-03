#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
char s[300];
int w[300];
int main ()
{
    while(gets(s))
    {
        int len = strlen(s), tt = 0, n = 0, min_ = 2147483645;
        for(int i = 0, f = 0; i <= len; i++)
        {
            if(s[i]==' '||s[i]==0) { if(f){w[n++] = tt; min_ = min_>tt?tt:min_; tt = 0; f = 0;} continue; }
            tt = (tt<<5)+s[i]-'a'+1;
            f = 1;
        }
        int next = min_, c, f = 1;
        while(f)
        {
            c = next; f = 0;
            for(int i = 0; i < n; i++)
            for(int j = i+1; j < n; j++)
            {
                if(c/w[i]%n==c/w[j]%n)
                {
                    f = 1;
                    tt = min((c/w[i]+1)*w[i],(c/w[j]+1)*w[j]);
                    next = max(tt,next);
                }
            }
        }
        printf("%s\n%d\n\n",s,c);
    }
    return 0;
}
