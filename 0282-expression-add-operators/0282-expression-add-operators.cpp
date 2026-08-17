using ll = long long;

class Solution {
public:
    vector<string> addOperators(string num, int target) {
		vector<string> res;
		// string op;
        sol(num, target, 0, "", res, 0, 0);
        return res;
		
    }
	void sol(string num, int t, int i, string op, vector<string>& res, ll c, ll p){
		// base case
		if (i == num.size()){
			if (c == t) {
				res.push_back(op);
			}
			return;
			
		}
		string cur;
		ll a = 0;
		for (int j = i; j < num.size(); j++){
			if (j > i && num[i] == '0') break;
			cur += num[j];
			a = a * 10 + num[j] - '0';

			if(i == 0){
				sol(num, t, j + 1, op + cur, res, a , a);
			}
			else{
				sol(num, t, j + 1, op + '+' + cur, res, c + a, a);
				sol(num, t, j + 1, op + '-' + cur, res, c - a, -a);
				sol(num, t, j + 1, op + '*' + cur, res, c - p + p * a, p * a);
			}


		}
	}
};