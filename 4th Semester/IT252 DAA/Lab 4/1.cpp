#include <bits/stdc++.h>

using namespace std;

void print_vector(vector<int> const &input)
{
	for (int i = 0; i < input.size(); i++) {
		cout << input.at(i) << ' ';
	}
}

int get_in_degree(int i,vector<int> const &edges){
	
	return 0;
}

int main(){

	int i,j,n_v,n_e,u,v;

	cout << "Enter the number of vertices" << endl;
	cin >> n_v;
	
	cout << "Enter the number of edges, followed by vertices of each edge" << endl;
	cin >> n_e; 

	vector < vector <int> > edges(n_e);
	vector < vector <int> > inverse_edges(n_e);

	int count[n_v];
	stack <int> S;

	for (i=0;i<n_e;++i){
		cin >> u >> v;
		edges[u].push_back(v);
		inverse_edges[v].push_back(u);
	}

	for (i=0;i<n_v;++i){
		count[i] = inverse_edges[i].size();
		if (count[i]==0)
			S.push(i);
	}

	cout << "Order of completion: ";

	while (S.size()>0){
		u = S.top();
		S.pop();
		cout << u << " ";

		for (i=0;i<edges[u].size();++i){
			v = edges[u][i];
			count[v]--;
			if(count[v]==0)
				S.push(v);
		}
	}

	cout << endl;
	
	return 0;
}