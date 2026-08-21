class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const table = {}

        for(const num of nums){
            table[num] = (table[num] ?? 0) + 1
        }

        return Object.entries(table)
            .sort((a, b) => b[1] - a[1])
            .slice(0, k)
            .map(([num]) => Number(num))    }
}
