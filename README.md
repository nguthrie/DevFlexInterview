These questions are used to assess a candidates level of comfort with programming and some computer science topics. 
If a candidate is unable to complete all the questions, this does not mean they have failed to qualify for the DevOps program. 
This will be decided in an interview. Candidates should be able to talk about the decisions they've made in when solving
these problems. It is strongly preferred that these solutions are provided in Python, as it is the most popular DevOps language
and is the language the tests are written in, but if a candidate would like to recreate the test in another language and 
can explain their solution to the interviewer, this is acceptable. Ideally, pytest question<n>.py will be called after submission
and all test will pass. 

There is no time limit. Please try your best and let us know how you find it. 


1. Write a function that selects the maximum value from an array of intergers. Do not use any built-in max functions.
select_max([1, 2, 3, 4]) -> 4


2. Write a function that takes an array of integers and centers all zeroes in the array. All non-zero integers should keep 
their relative position. For the purpose of this question, center means floor(length of array / 2). 
center_zeros([1, 1, 3, 0, 6, 0]) -> [1, 1, 0, 0, 3, 6]


3. Students have been assigned a series of math problems that have points associated with them. Given a sorted points 
array, minimize the number of problems a student needs to solve based on the criteria below:

a. They must always solve the first problem, index i = 0
b. After solving the ith problem, they have a choice: solve the next problem (i +1) or skip ahead and work the (i+2) problem.
c. Students must keep solving problems until the difference between the maximum points and the minimum points questions
 solved so far meets or exceeds a specified threshold
d. If a student cannot meet or exceed the threshold, they must work through all the problems. 

Return the minimum number of problems a student needs to solve. 

minimum_points(2, [1, 2, 3]) -> 2
Explanation: if a student solves points[0] = 1, points[2] = 3, the difference between the minimum and the maximum points
 solved is 3 - 1 = 2. This meets the threshold, so the student must solve at least 2 problems. Return 2. 

minimum_points(4, [1, 2, 3, 5, 8]) -> 3
If the threshold is 4, again it takes 3 problems solving problems 1, 3 and 4 where points[3] - points[0] = 5 - 1 = 1.
 This meets the threshold, so the student must solve at least 3 problems. Return 3


Please see the test cases for more examples of input to output mappings for each question. 

Good luck!