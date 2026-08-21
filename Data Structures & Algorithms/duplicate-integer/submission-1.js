class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let seen = {}

        for(const n of nums){
            if(seen[n]){
                return true
            }
            seen[n] = true
        }

        return false
    }
}
