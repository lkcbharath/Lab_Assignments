#include <bits/stdc++.h>

using namespace std;
// define funcs here

void printArray(int arr[], int n){
	for (int i=0;i<n;++i){
		printf("%d ",arr[i]);
	}
	printf("\n");
}

bool proposedToAll(int arr[], int n){
	bool status = false;
	int count = 0;
	for (int i = 0; i < n ; ++i){
		if (arr[i]==n){
			++count;
		}
	}

	if (count==n)
		return true;

	return false;
}

//UNFINISHED

int main(){

	
	int n = 5,i,j,m,w,m_curr;

	queue <int> q;

	for (i=0;i<n;++i){
		q.push(i);
	}

	int wife[] = {-1,-1,-1,-1,-1};
	int husband[] = {-1,-1,-1,-1,-1};
	int count[] = {0,0,0,0,0};

	// assume to be inversed;
	int men_pref_list[n][n] = {
		{1,2,0,4,3},
		{1,3,2,4,0},
		{4,0,1,3,2},
		{4,0,2,1,3},
		{2,1,3,4,0}};

	int women_pref_list[n][n] = {
		{1,2,0,4,3},
		{1,3,2,4,0},
		{1,0,4,3,2},
		{0,4,2,1,3},
		{2,1,3,4,0}};

	

	//propose them yo

	while((!q.empty()) && !proposedToAll(count,n)){

		m = q.front();
		w = men_pref_list[m][count[m]];
		m_curr = husband[w];

		if (m_curr==-1){
			cout << m << w << endl;
			wife[m] = w;
			husband[w] = m;
			q.pop();
		}

		else if (women_pref_list[w][m] < women_pref_list[w][m_curr]){
			q.pop();
			wife[m] = w;
			husband[w] = m;
			wife[m_curr] = -1;
			q.push(m_curr);
		}

		++count[m];
	}



	return 0;
}