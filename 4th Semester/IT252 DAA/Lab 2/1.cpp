#include <bits/stdc++.h>
using namespace std;

int solve_hanoi(int n, char s, char i, char t){
	if (n){
		solve_hanoi(n-1,s,t,i);
		printf("moved disk %d from %c to %c\n",n,s,t);
		solve_hanoi(n-1,i,s,t);
	}
}

int main(){
	int n;
	cout << "Enter the number of disks: ";
	cin >> n;
	// if (typeof)
	solve_hanoi(n,'s','i','t');
}