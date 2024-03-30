/**
 * 
 *数组求和问题：
 
 */
// 给定一个正整数数组和一个目标值，请你在该数组中找出两个相加等于目标值的两个正整数，并返回他们的下标。
function findSumTarget(nums,target){
    const {length} = nums
    const dirrs = {}
    for(let i;i<length;i++){
        if(dirrs[target-nums[i]] !== undefined) return [dirrs[target - num[i]],i]
        dirrs[nums[i]] = i
    }
}

// 双指针法