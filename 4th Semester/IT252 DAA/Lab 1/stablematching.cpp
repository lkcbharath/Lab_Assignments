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

	string line;

  

	// ifstream myfile ("input.txt");
 //    if (myfile.is_open()){
 //    	while (getline (myfile,line)){
 //    		if (line!=""){
 //      			cout << line << '\n';
 //    		}
 //      }
 //    myfile.close();
 //  	}

	queue <int> q;

	for (i=0;i<n;++i){
		q.push(i);
	}

	int wife[] = {-1,-1,-1,-1,-1};
	int husband[] = {-1,-1,-1,-1,-1};
	int count[] = {0,0,0,0,0};

	// assume to be inversed;
	int men_pref_list[n][n] = {
		{1,0,3,4,2},
		{3,1,0,2,4},
		{1,4,2,3,0},
		{0,3,2,1,4},
		{1,3,0,4,2}};

	int women_rank_list[n][n] = {
		{1,2,4,3,0},
		{3,1,0,2,4},
		{4,0,1,2,3},
		{0,4,3,2,1},
		{4,1,3,0,2}};

	

	//propose them yo

	while((!q.empty()) && !proposedToAll(count,n)){

		m = q.front();
		w = men_pref_list[m][count[m]];
		m_curr = husband[w];

		if (m_curr==-1){
			wife[m] = w;
			husband[w] = m;
			q.pop();
		}

		else if (women_rank_list[w][m] < women_rank_list[w][m_curr]){
			q.pop();
			wife[m] = w;
			husband[w] = m;
			wife[m_curr] = -1;
			q.push(m_curr);
		}

		++count[m];
	}

	for (i=0;i<n;++i){
		cout << i << wife[i] << endl;
	}



	return 0;
}