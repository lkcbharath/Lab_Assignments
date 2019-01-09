#include <bits/stdc++.h>

using namespace std;
// define funcs here






//UNFINISHED



int main(){

	
	int n = 5,i,j;

	queue <int> q;

	for (i=0;i<n;++i){
		q.push(i);
	}

	int wife[] = {-1,-1,-1,-1,-1};
	int husband[] = {-1,-1,-1,-1,-1};
	int count[] = {0,0,0,0,0};

	// assume to be inversed;
	int men_pref_list[n][n] = {{1,2,0,4,3},
	{3,1,2,4,0},
	{4,0,1,3,2},
	{0,4,2,1,3},
	{2,1,3,4,0}};

	int women_pref_list[n][n] = {{1,2,0,4,3},
	{3,1,2,4,0},
	{4,0,1,3,2},
	{0,4,2,1,3},
	{2,1,3,4,0}};

	

	//propose them yo

	while(!q.empty() && count[q.front()]!=n){
		int m = q.pop();

		int w = men_pref_list[m][count[m]];

		int m_curr = husband[w];

		if (m_curr==-1){
			wife[m] = w;
			husband[w] = m;
		}
		else if (
			women_pref_list[w][m] >
			//current
			women_pref_list[w][m_curr]
			){
			wife[m] = w;
			husband[w] = m;
			wife[m_curr] = -1;
			q.push(m_curr);
		}

		++count[m];
	}



	return 0;
}