#include <bits/stdc++.h>

using namespace std;

bool sortbysec(const pair<int,int> &a, 
              const pair<int,int> &b) 
{ 
    return (a.second < b.second); 
} 

int main(){

	int n,i,u,v,finish_time;
	cout << "Enter the number of intervals: ";
	cin >> n;
	vector< pair <int,int> > intervals; 

	cout << "Enter each interval's start and end time" << endl;

	for(i=0;i<n;++i){
		cin >> u >> v;
		intervals.push_back(make_pair(u,v));
	}

	sort(intervals.begin(), intervals.end(), sortbysec);

	finish_time = intervals[0].second;

	for(i=1;i<intervals.size();++i){
		if (intervals[i].first<finish_time){
			intervals.erase (intervals.begin()+(i--));
		else
			finish_time = intervals[i].second;
	}

	for(i=0;i<intervals.size();++i){
		cout << "[" << intervals[i].first << "," << intervals[i].second << "] ";
	}
	cout << endl;
	return 0;
}