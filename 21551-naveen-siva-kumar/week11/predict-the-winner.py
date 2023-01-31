class Solution {

public: int helper(int i,int j,vector<int>& nums,vector<vector<int>>& dp){
        if(i>j) 
            return 0;
		if(dp[i][j]!=-1)
             return dp[i][j];
		int a= nums[i]+ min(helper(i+2,j,nums,dp),helper(i+1,j-1,nums,dp));
		int b= nums[j]+ min(helper(i+1,j-1,nums,dp),helper(i,j-2,nums,dp));
		return dp[i][j]=max(a,b);
}


public:
    bool PredictTheWinner(vector<int>& nums) {
        vector<vector<int>> dp(nums.size(),vector<int>(nums.size(),-1));
        if (nums.size()==1){
             return true;
        }
        int total_sum=accumulate(nums.begin(), nums.end(), 0);
        int p1_sum = helper(0,nums.size()-1,nums,dp);
        if(p1_sum-(total_sum-p1_sum)>=0){
            return true;
        }else{
            return false;
        }

    }
};
