# avant-challenge

#factors_and_caching (ruby)

**Run factors_and_caching.rb in the command line (ruby factors_and_caching.rb)**

Accomplish in a language of your choice:

Input: Given an array of integers

Output: In whatever representation you wish, output each integer in the array and all the other integers in the array that are
factors of the first integer.  

Example:

  Given an array of [10, 5, 2, 20], the output would be:

{10: [5, 2], 5: [], 2: [], 20: [10,5,2]}

Additional Questions: 

1.  What if you were to cache the calculation, for example in the file system.  What would an example implementation
of the cache look like?  By cache I mean, given an array input, skip the calculation of the output if you have already
calculated the output at least once already.

**Answer:** My implementation of a cache uses memoization to store and access the factorizations calculated from the given array. In the event of duplicates, memoization would speed up the method considering that some of the calculations would be skipped. In my specific case, the use of caching(memoization) did not affect the run time since the arrays were composed of unique integers.

2.  What is the performance of your caching implementation?  Is there any way to make it more performant.

**Answer:** My implementation, which uses ruby dictionaries (hash maps), has a linear run time. As mentioned before, my example uses arrays that don’t have any duplicates. The performance can be improved, for instance, through the use of more efficient factoring algorithms or by having sorted arrays. Sorting the arrays would speed up the search for duplicates. More efficient data structures can also be used to reduce run time(i.e. Struct vs Hash).

3.  What if you wanted to reverse the functionality.  What if you wanted to output each integer and all the other integers in the 
array that is the first integer is a factor of I.E:

Given an array of [10, 5, 2, 20], the output would be:
{10: [20], 5: [10,20], 2: [10, 20], 20: []}

Would this change your caching algorithim?

With caching, the output should be the same except the calculations are not performed.

**Answer:** In my code you would replace “if num1%num2 ==0 and num1!=num2” with “if num2%num1 ==0 and num1!=num2”. This changes the nested loop to see whether the first number is a factor of the second number (num2%num1==0). Everything else would remain the same including the caching algorithm.

#twitter_test (python w/ Python Twitter Tools library for handling the API)

**Run twitter_test.py in the command line (python twitter_test.py). This will print the ten most frequent words from the stream. Output1.txt and output2.txt will be created along the way.**

As a quick tech evaluation I'd like you to use the Twitter streaming API (statuses/sample) to collect 5 minutes of tweets.
 Obtain a total word count, filter out "stop words" (words like "and", "the", "me", etc -- useless words),
 and present the 10 most frequent words in those 5 minutes of tweets. 

Please don't copy and paste any code, but of course you can do whatever research necessary.
 Your code should be clear to follow, with explanatory comments where necessary. 

Let me know if you have any questions about this (and also please confirm that you understand the project),
 and I look forward to seeing what you come up with!

Optional Part B) How would you implement it so that if you had to stop the program and restart,
 it could pick up from the total word counts that you started from?
