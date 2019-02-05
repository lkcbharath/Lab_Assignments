#include <bits/stdc++.h>

using namespace std;

void printArray(int arr[], int n){
	for (int i=0;i<n;++i){
		printf("%d ",arr[i]);
	}
	printf("\n");
}

int main(){

	int n=0,i,j,m,w,m_curr=0;

	string line,word;

	map<char,int> men,women;

	map<char,string> men_strings,women_strings;

	vector<vector<int> > men_pref_list,women_rank_list; //rank list is inversed;
	vector<int> temp;

	ifstream myfile ("input.txt");	
    if (myfile.is_open()){
		for(i=0;i<2;++i) {
			j=0;
			getline (myfile,line);
			stringstream ssin(line);
			while (ssin.good()){
				ssin >> word;
				if (i==0){
					men[word[0]] = j;
					men_strings[word[0]] = word;
					++n;
				}
				else{
					women[word[0]] = j;
					women_strings[word[0]] = word;
				}
				++j;
			}
      	}

		getline(myfile,line); // empty string

		for (i=0;i<n;++i){
			temp.clear();
			getline(myfile,line);
			stringstream ssin(line);
			while (ssin.good()){
				ssin >> word;
				temp.push_back(women[word[0]]);
				
			}
			men_pref_list.push_back(temp);
		}

		getline(myfile,line); // empty string

		for (i=0;i<n;++i){
			temp.clear();
			temp.resize(n);
			getline(myfile,line);
			stringstream ssin(line);
			j=0;
			while (ssin.good()){
				ssin >> word;
				temp[men[word[0]]] = j;
				++j;	
			}
			women_rank_list.push_back(temp);
		}
		
    	myfile.close();
  	}

	queue <int> q;
	for (i=0;i<n;++i){
		q.push(i);
	}

	int wife[] = {-1,-1,-1,-1,-1};
	int husband[] = {-1,-1,-1,-1,-1};
	int count[] = {0,0,0,0,0};
	int proposed_count = 0;

	while((!q.empty()) && proposed_count!=n){

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
		if (count[m]==n)
			++proposed_count;
	}

	ofstream file { "output.txt" };

	ofstream outputfile;
	outputfile.open("output.txt");

	for (i=0;i<n;++i){
		char key_women,key_men;
		
		for (auto &mm : men) {
			if (mm.second == husband[i]) {
				key_men = mm.first;
				break; // to stop searching
			}
		}

		for (auto &w : women) {
			if (w.second == wife[i]) {
				key_women = w.first;
				break; // to stop searching
			}
		}
		outputfile << men_strings[key_men] << " " <<  women_strings[key_women] << "\n";
	}

	outputfile.close();

	return 0;
}