# Arrays and Hashing

This section contains the following problems:

[217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) (easy)

[242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) (easy)

[1. Two Sum](https://leetcode.com/problems/two-sum/) (easy)

[49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) (medium)

[347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) (medium)

[271. Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) (medium) (PREMIUM)

[238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) (medium)


Below are some personal notes about the problems.

### 217. Contains Duplicate

Date: 23.01.2025

Runtime: 4ms (90.77%)

Memory: 31.54MB (43.04%)

Nothing to say there.

### 242. Valid Anagram

Date: 23.01.2025

Runtime: 5ms (93.55%)

Memory: 17.87MB (48.55%)

Nice use of Counters.

### 1. Two Sum

Date: 23.01.2025

Runtime: 0ms (100%) 

Memory: 18.91MB (22.62%)

Compute `target - x` and using a dictionary to solve the problem in O(n)

### 49. Group Anagrams

Date: 23.01.2025

Runtime: 11ms (83.37%) 

Memory: 20.59MB (74.80%)

I kept going for the bruteforce method with Counters because of the previous anagram problem... Then I remembered the sorting trick. 

### 347. Top K Frequent Elements

Date: 23.01.2025

Runtime: 4ms (71.54%)

Memory: 21.30MB (47.79%)

One liner, that uses a built-in function. I'm not reinventing the wheel :\)

I'm definitely remembering the heapq method though. 

### 271. Encode and Decode Strings

Date: 23.01.2025

Don't have the scores for this one. (PREMIUM)
Relatively easy problem, just had to think of a nice way to encode. Got reminded of Run-Length Encoding (thank you, ENSEA) and went with it. Ultimately, the encoded string looks like this: 

`"l0#w0l1#w1l2#w2l3#w3l4#w4l5#w5"`

Where `ln` is the length of the n-th word `wn`. The delimiter could be any character as long as it's not a digit (otherwise it messes up with the stop condition).

### 238. Product of Array Except Self
