'''So, as usual, one of my CodeWars solutions was beaten out by an
   extremely snazzy one-liner (for the digital root program)

   The code there is as follows:
   def digital_root(n):
       return n if n < 10 else digital_root(sum(map(int, str(n))))

   So, I've just reverse-engineered how sum() and map() can work together to
   accomplish a simple step - summing digits of a given int.

   The following is my example solution:'''

def digital_sum(n):
    return sum(map(int, str(n)))

print(digital_sum(942))
