The program finds the largest integer value out of variables a, b and c.

**1.3**  
Tracing the algorithm when `a = 4`, `b = -5` and `c = 1`:
| a | b | c | result |
| - | - | - | - |
| 4 | -5 | 1 | 4 |

The algorithm outputs 4, which is the value of a, since it has the largest value.
Case: b > c > a  
First, the program assumes that result = a.  
Then, it checks whether b > result. Since b > a, this is true, so result = b.  
Lastly, it checks whether c > result. Since c < b, the result remains unchanged.  
The program then prints the result, which is the largest number of the three. In this case that's b. 