/*
 * @lc app=leetcode.cn id=62 lang=javascript
 *
 * [62] 不同路径
 */

// @lc code=start
/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
console.log("递归-------");
function dp_function(m ,n) {
    if (m == 1 || n == 1){
        return 1;
    }

    if (m == 2 && n == 2){
        return 2;
    }
     
    return dp_function(m-1,n) + dp_function(m,n-1);
}
console.log(dp_function(3,3));


console.log("递归+记忆搜索------");
function dp_function_canche(m ,n, cacheMap) {
    if (m == 1 || n == 1){
        return 1;
    }

    if (m == 2 && n == 2){
        return 2;
    }
    var key = m + ',' + n;
    if (cacheMap.has(key)) {
        return cacheMap.get(key);
    }
    var value = dp_function_canche(m-1,n,cacheMap) + dp_function_canche(m,n-1,cacheMap);
    cacheMap.set(key,value);
    return value;
}

var cacheMap = new Map();
console.log(dp_function_canche(3,3,cacheMap));

console.log("自底向上：迭代------");
function dp_fs(m,n){
    //边界条件
    if (m <= 0 || n <= 0){
        return 0;
    }
    if (m == 1 || n == 1){
        return 1;
    }
    if(m == 2 && n == 2){
        return 2;
    }
    //初始化
    var dp = [];
    for(var i = 0; i < m; i++){
        dp[i] = [];
        for(var j = 0; j < n; j++){
            dp[i][j] = 0;
        }
    }
    //这里是给初始化做的补充，m == 1 或者 n == 1 时只有一种路径
    for(var i = 0; i < m; i++){
        dp[i][0] = 1;
    }
    for(var j = 0; j < n; j++){
        dp[0][j] = 1;
    }
    //迭代
    for(var i = 1; i < m; i++){
        for(var j = 1; j < n; j++){
            dp[i][j] = dp[i-1][j] + dp[i][j-1];
            
        }
    }
    return dp[m-1][n-1];
}
console.log(dp_fs(7,3));


console.log("自底向上：迭代2------");
function dp_fs_two(m,n){
    if (m <= 0 || n <= 0){
        return 0;
    }
    if (m == 1 || n == 1){
        return 1;
    }
    if(m == 2 && n == 2){
        return 2;
    }

    var dp = [];
    for(var i = 0; i < m; i++){
        for(var j = 0; j < n; j++){
            if (i == 0 || j == 0){
                dp[i+m*j] = 1;
            }else{
                dp[i+m*j] = 0;
            }
            
        }
    }
    for(var i = 1; i < m; i++){
        for(var j = 1; j < n; j++){
            dp[i+m*j] = dp[(i-1)+m*j] + dp[i+m*(j-1)];
            
        }
    }
    return dp[(i-1)+m*(j-1)];
}
console.log(dp_fs_two(2,3));
//
// @lc code=end
