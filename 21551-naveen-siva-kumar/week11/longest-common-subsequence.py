class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int dp[text2.size()+1][text1.size()+1];
        memset(dp,0,sizeof(dp));
        int i,j;
        for(i=1;i<=text2.size();i++){
            for(j=1;j<=text1.size();j++){
                if(text2[i-1]==text1[j-1]){
                        //cout<<"text2[i]"<<i<<"text1[j]"<<j<<endl;
                        dp[i][j] = dp[i-1][j-1]+1;
                }
                else{
                    
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
                }
            }
        }
        // for (i=1;i<=text2.size();i++){
        //     for(j=1;j<=text1.size();j++){
        //         cout<<dp[i][j]<<" ";
        //     }cout<<endl;
        // }
        return dp[text2.size()][text1.size()];
    }
};
