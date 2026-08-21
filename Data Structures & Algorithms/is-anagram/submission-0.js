class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const seen = {}
        
        for(const c of s){
            if(!seen[c]){
                seen[c] = 1
            } else {
                seen[c] += 1
            }
        }

        for(const c of t){
            if(!seen[c]){
                return false
            }

            seen[c] -= 1
        }

        return Object.values(seen).filter((v) => v !== 0).length !== 0 ? false : true
    }
}
