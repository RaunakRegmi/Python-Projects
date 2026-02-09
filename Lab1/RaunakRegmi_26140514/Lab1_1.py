# Lab1_1  Exercise #3.1
#
# A program to compute the sum, average, and sum of cubes of 3 numbers.
#

A = float( input( "\nEnter the number A: \n" ) )

B = float( input( "\nEnter the number B: \n" ) )

C = float( input( "\nEnter the number C: \n" ) )

#Display the numbers

print( "\nThe numbers are:\n" )
print( "  Number A = ", A )
print( "  Number B = ", B )
print( "  Number C = ", C )

# ****Modify that program to the sum, average, and sum of cubes of 3 numbers. ****

tot = A + B + C  # replace 0.0 with the sum.
average = tot / 3 # replace 0.0 with the average.
sum_of_cubes = (A ** 3) + (B ** 3) + (C ** 3) # replace 0.0 with the sum of cubes of the numbers.

# Output the results

print( "The sum is", tot)
print( "The average is", average)
print("The sum of cubes is", sum_of_cubes)