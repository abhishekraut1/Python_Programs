#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void fastscan(int &number)
{
    bool negative = false;
    register int c;
    number = 0;

    c = getchar();
    if (c=='-')
    {
        negative = true;
        c = getchar();
    }

    for (; (c>47 && c<58); c=getchar())
        number = number *10 + c - 48;
 
    if (negative)
        number *= -1;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 

   int t;
   fastscan(t);
   while(t-->0){
       int c = 0, p = -1;
            string str;
            cin>>str;
            int n = str.length();
            if (n == 1) {
                cout<<"NO"<<endl;
                continue;
            }
            for (int i = 0; i < n; i++) {
                if (str[i] == '1') {
                    c++;
                    p = i + 1;
                }
            }
             if (c == 0 || (c == 1 && p == n)) {
               cout<<"NO";
            } else {
                cout<<"YES";
            }
   }
}