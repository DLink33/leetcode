// Longest Common Prefix //

/*
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

NOTES:
This looks like a two/multi pointer solution to me.  Pretty straight forward. One pointer per string.  We start at the beginning and we progress down each string until we don't see a match.  For every match we find, we add it to the output string.  We stop adding once a discrepancy is found.

 We will want to iterate a maximum of the shortest length string. 
*/


function getSmallestStr(strs) {
    
    let smallest = strs[0];
    let min = smallest.length;
    for (const str of strs.slice(1)) {
        let currLen = str.length;
        if (currLen < min) {
            min = currLen;
            smallest = str;
        }
    }
    return smallest;
}

/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    const smallest = getSmallestStr(strs);
    const n = smallest.length;
    let rslt = "";
    for(let i = 0; i < n; ++i) {
        for (const str of strs) {
            if(str[i] !== smallest[i]) return smallest.slice(0,i);
        }
    }
    return smallest;
};

function main() {
    /*
    Input: strs = ["flower","flow","flight"]
    Output: "fl"
    */

    const strs = ["flower","flow","flight"];
    let result = longestCommonPrefix(strs);
    console.log(result);
}

main();