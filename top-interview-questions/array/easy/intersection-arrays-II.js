// Intersection of Two Arrays II

/*
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

NOTES:
If you compare every eleme of one array with every elem of the other array you can create final array
with all of the elements present in both.  The issue with this is you have to be able to account for duplicates. 
Another idea is to create a Map of the smaller of the two arrays (a little more space efficient), where the key is the elem and the value is the count. I think either the traditional obj in JS or the Map() object might be good for this. You would then iterate through the second array if the value is in the map of the first array's frequency and the count is > 0, you would decrement and add that value to a resultant array. 

If you sort both arrays prior, you can use a two-pointer technique to increment through both array's simultaneously. If the values are different, increment only the smaller of the two pointers. If the are equal, add the value at that position (in either array) to the resultant array, and increment both pointers.  Loop like this until you have reached the end of either input array.

*/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function (nums1, nums2) {
  let arr1 = [];
  let arr2 = [];
  if (nums1.length < nums2.length) {
    arr1 = nums1;
    arr2 = nums2;
  } else {
    arr1 = nums2;
    arr2 = nums1;
  }

  let numsMap = {};
  let rslt = [];
  for (const e of arr1) {
    if (Object.hasOwn(numsMap, e)) numsMap[e]++;
    else numsMap[e] = 1;
  }
  for (const e of arr2) {
    if (Object.hasOwn(numsMap, e)) {
      if (numsMap[e] > 0) {
        numsMap[e]--;
        rslt.push(e);
      }
    }
  }

  return rslt;
};

function swap(arr, idx1, idx2) {
  let temp = arr[idx1];
  arr[idx1] = arr[idx2];
  arr[idx2] = temp;
}

function selectionSort(arr) {
  const n = arr.length;
  for (let i = 0; i < n - 1; i++) {
    let min_dex = i;
    for (let k = i + 1; k < n; k++) {
      if (arr[k] < arr[min_dex]) min_dex = k;
    }
    if (min_dex != i) swap(arr, i, min_dex);
  }
}

// two pointer solution using sort
// more space efficient (possibly more time efficient too)
var intersetWithSort = function (nums1, nums2) {
  selectionSort(nums1);
  selectionSort(nums2);
  const len1 = nums1.length;
  const len2 = nums2.length;
  let a = 0;
  let b = 0;
  let rslt = [];
  while (a < len1 && b < len2) {
    let val1 = nums1[a];
    let val2 = nums2[b];
    if (val1 === val2) {
      rslt.push(val1);
      a++;
      b++;
    } else if (val1 < val2) {
      a++;
    } else {
      b++;
    }
  }
  return rslt;
};

const main = function () {
  const nums1 = [1, 2, 2, 1];
  const nums2 = [2, 2];
  console.info(intersect(nums1, nums2));

  const nums3 = [4, 9, 5];
  const nums4 = [9, 4, 9, 8, 4];
  console.info(intersetWithSort(nums3, nums4));
};

main();
