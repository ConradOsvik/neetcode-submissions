class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        const encoded = []

        for(const str of strs){
            const l = str.length

            encoded.push(`${l}#${str}`)
        }

        return encoded.join("")
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        const decoded = []

        console.log(str)

        let start = 0
        for(let i = 0; i < str.length; i++){
            if(str[i] === "#"){
                console.log(i, start)

                const count = Number(str.slice(start, i))
                console.log(str.slice(start, i))
                const j = i + 1
                decoded.push(str.slice(j, j + count))

                start = i + 1 + count
                i += count + 1
            }
        }

        return decoded
    }
}
