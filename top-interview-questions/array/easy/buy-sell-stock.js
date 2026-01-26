/* eslint-disable no-undef */
//   Best Time to Buy and Sell Stock II

/*
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

Find and return the maximum profit you can achieve.

NOTES:
So the first intution here is that this is a dynamic programming problem, but I think it should be simpler than that. 
If we can only gain profit day to day with an increasing price, then we need to track which days are increasing and which days are decreasing. Any set of days were the price decreases we ignore since it would only serve to lose us money.  Tracking days of increasing values we can sum these up and that should be the max amount we can make over the course of the week.

Another way of phrasing it:
  - You want to be holding the stock during every upward step
  - You want to be out of the stock during every downward step
  - Summing positive adjacent differences enforces exactly that

You never:
  - hold through a drop
  - double-count gains
  - violate the “at most one share” rule

You could think of this as being able to see 1 day into the future.  If you see that the price is going to go down tomorrow, then you sell what you have and wait for tomorrow to come. You then perform the same analysis, if the price is going to go up. then you buy and wait until the next day to sell.  Tomorrow comes, you sell, and perform the analysis again.


SOLUTION:
Iterate through the array in pairs until we reach the end of week. If arr[i] - arr[i-1] <= 0, ignore it.  If it is > 0, add to running total. At the end of the iteration, return running total.

TIME ANALYSIS:
O(n)

SPACE ANALYSIS:
O(1)

*/

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  const n = prices.length;
  let total = 0;
  for (let i = 1; i < n; ++i) {
    let diff = prices[i] - prices[i - 1];
    if (diff > 0) total += diff;
  }
  return total;
};

function main() {
  const prices = [7, 1, 5, 3, 6, 4];
  let rslt = maxProfit(prices);
  console.log(rslt);
}

main();
