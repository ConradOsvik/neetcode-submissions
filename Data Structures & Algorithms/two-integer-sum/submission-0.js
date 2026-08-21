class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const values = new Map()

        for(let i = 0; i < nums.length; i++){
            const n = nums[i]
            const diff = target - n

            if(values.get(diff) !== undefined){
                return [values.get(diff), i]
            }

            values.set(n, i)
        }
    }
}
