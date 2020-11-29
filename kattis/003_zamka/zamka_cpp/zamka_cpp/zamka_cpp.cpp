/*
# https://open.kattis.com/problems/zamka
# The impossible has happened.Bear G.has fallen into his own trap.
# Lured by a delicious box of Domaćica, without even thinking, he rushed
#and fell into his trap.In order to get out of the trap, he must solve
# the following task with your help.You are given three integers L, Dand X.
#
# - determine the minimal integer N such that L≤N≤D and the sum of its digits is X
# - determine the maximal integer M such that L≤M≤D and the sum of its digits is X
#
# Bear will be able to escape from the trap if he correctly determines numbers N
#and M.The numbers Nand M will always exist.
#
# Input
# The first line of input contains the integer L(1≤L≤10000), the number from
# the task.The second line of input contains the integer D(1≤D≤10000, L≤D),
# the number from the task.The third line of input contains the integer X(1≤X≤36),
# the number from the task.
#
# Output
# The first line of output must contain the integer N from the task.The second
# line of output must contain the integer M from the task.

*/


#include <iostream>
#include <string>

int main()
{
    int lower_bound, upper_bound, target_sum_of_digits;

    std::cin >> lower_bound;
    std::cin >> upper_bound;
    std::cin >> target_sum_of_digits;

    int min_number_fit = 100000;
    int max_number_fit = 0;
    for (int i = lower_bound; i <= upper_bound; ++i) {
        std::string s = std::to_string(i);
        int digits_sum = 0;
        for (int num_digit = 0; num_digit < s.size(); ++num_digit) {
            char sd = s.at(num_digit);
            int digit = int(sd)-int('0');
            digits_sum += digit;
        }
        if (digits_sum == target_sum_of_digits) {
            if (i < min_number_fit) {
                min_number_fit = i;
            }
            if (i > max_number_fit) {
                max_number_fit = i;
            }
        }
    }

    std::cout << min_number_fit << '\n';
    std::cout << max_number_fit << '\n';
}
