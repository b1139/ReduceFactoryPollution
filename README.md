# ReduceFactoryPollution
Question Asked on Codility

N factories are producing pollution. Given pollution amount in terms of integers. Count mini. no. of filters required to reduce total pollution by atleast half. One filter reduces pollution by half.

A company has N factories, each producing some pollution every month. The company has decided to reduce its total fume emissions by equipping some of the factories with one or more filters.

Every such filter reduces the pollution of a factory by half. When a second (or subsequent) filter is applied, it again reduces by half the remaining pollution emitted after fitting the existing filter(s). For example, a factory that initially produces 6 units of pollution will generate 3 units with one filter, 1.5 units with two filters and 0.75 units with three filters.

You are given an array of N integers describing the amount of pollution produced by the factories. Your task is to find the minimum number of filters needed to decrease the total sum of pollution by at least half.

Write a function:
class Solution { public int solution(int(] A); }
which, given an array of integers A of length N, returns the minimum number of filters needed to reduce the total pollution by at least half.

Example: 1. 
  Given A = [5, 19, 8, 1], your function should return 3. The initial total pollution is 5 + 19 + 8 + 1 = 33. 
  We install two filters at the factory producing 19 units and one filter at the factory producing 8 units. 
  Then the total pollution will be 5 + ((19 / 2)/ 2) + (8 / 2) + 1 = 5 + 4.75 + 4 + 1 = 14.75 which is less than 33 / 2 = 16.5, so we have achieved our goal.
Example: 2. 
  Given A = [10, 10], your function should return 2, because we may install one filter at each factory.
