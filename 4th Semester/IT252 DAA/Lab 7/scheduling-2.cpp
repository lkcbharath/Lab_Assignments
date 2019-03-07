#include <bits/stdc++.h>

using namespace std;

bool sortbyfirst(const pair<int,int> &a, 
              const pair<int,int> &b) 
{ 
    return (a.first < b.first); 
} 

int main(){

	int l,n,m,i,j,k,u,v,finish_time, new_group_flag;
	cout << "Enter the number of intervals: ";
	cin >> n;
	vector< pair <int,int> > intervals; 

	pair <int,int> current_interval,check_interval_left,check_interval_right;

	cout << "Enter each interval's start and end time" << endl;

	for(i=0;i<n;++i){
		cin >> u >> v;
		intervals.push_back(make_pair(u,v));
	}

	sort(intervals.begin(), intervals.end(), sortbyfirst);

	vector< vector< pair <int,int> > > allocations;

	vector< pair<int,int> > temp = { intervals[0] };

	allocations.push_back(temp);

	// cout << allocations[0][0].first << allocations[0][0].second;
	for(i=1;i<n;++i){
		current_interval = intervals[i];

		m = allocations.size();
		
		new_group_flag = 1;

		//somewhere inside, set to 0
		for(j=0;j<m;++j){

			l = allocations[j].size();

			if (current_interval.second < allocations[j][0].first){
				allocations[j].insert(allocations[j].begin(),current_interval);
				new_group_flag = 0;
				break;
			}

			for(k=1;k<l-1;++k){
				check_interval_left = allocations[j][k];
				check_interval_right = allocations[j][k+1];


				if (current_interval.first > check_interval_left.second && current_interval.second < check_interval_right.first){
					allocations[j].insert(allocations[j].begin()+k+1,current_interval);
					new_group_flag = 0;
					break;
				}

			}

			if ((new_group_flag) && current_interval.first > allocations[j][l-1].second){
				allocations[j].insert(allocations[j].begin()+l,current_interval);
				new_group_flag = 0;
				break;
			}

		}

		if (new_group_flag){
			vector< pair<int,int> > temp2 = { current_interval };
			allocations.push_back(temp2);
		}


	}

	n = allocations.size();

	for (i=0;i<n;++i){
		m = allocations[i].size();
		for(j=0;j<m;++j){
			cout << "[" << allocations[i][j].first << "," << allocations[i][j].second << "] ";
		}
		cout << endl;
	}

	return 0;
}