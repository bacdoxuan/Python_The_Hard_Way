# Symbol review

# Keywords
and
del
from
not
while
as
elif
global
or
with
assert
else
if
pass
yield
break
except
Exception
import
print
class
exec
in
raise
continue
finally
is
return
def
for
lambda
try

# Data type
True
False
None
string
number
float
list
tuple
set
dict
orderdict
defaultdict
dequeue


# string sequence escape
"""
Escape Sequence     Meaning     Notes
\n  newline    Backslash and newline ignored
\\  Backslash (\)
\'  Single quote (')
\"  Double quote (")
\a  ASCII Bell (BEL)
\b  ASCII Backspace (BS)
\f  ASCII Formfeed (FF)
\n  ASCII Linefeed (LF)
\r  ASCII Carriage Return (CR)
\t  ASCII Horizontal Tab (TAB)
\v  ASCII Vertical Tab (VT)
\ooo    Character with octal value ooo  (1,3)
\xhh    Character with hex value hh     (2,3


In [3]: print("This \\ is a test string")
This \ is a test string

In [4]: print("This \' is a test string")
This ' is a test string

In [5]: print("This \" is a test string")
This " is a test string

In [6]: print("This \a is a test string")
This  is a test string

In [7]: print("This \b is a test string")
This is a test string

In [8]: print("This \f is a test string")
This
      is a test string

In [9]: print("This \n is a test string")
This
 is a test string

In [10]: print("This \r is a test string")
 is a test string

In [11]: print("This \t is a test string")
This     is a test string

In [12]: print("This \v is a test string")
This
      is a test string

"""


""" string format (old style)
%s  Format a string. For example, '%-3s' % 'xy' yields 'xy '; the width (-3) forces left alignment.
%d  Decimal conversion. For example, '%3d' % -4 yields the string ' -4'.
%e  Exponential format; allow four characters for the exponent. Examples: '%08.1e' % 1.9783 yields '0002.0e+00'.
%E  Same as %e, but the exponent is shown as an uppercase E.
%f  For float type. E.g., '%4.1f' % 1.9783 yields ' 2.0'.
%g  General numeric format. Use %f if it fits, otherwise use %e.
%G  Same as %G, but an uppercase E is used for the exponent if there is one.
%o  Octal (base 8). For example, '%o' % 13 yields '15'.
%x  Hexadecimal (base 16). For example, '%x' % 247 yields 'f7'.
%X  Same as %x, but capital letters are used for the digits A-F. For example, '%04X' % 247 yields '00F7'; the leading zero in the length (04) requests that Python fill up any empty leading positions with zeroes.
%c  Convert an integer to the character with the corresponding ASCII code. For example, '%c' % 0x61 yields the string 'a'.
%%  Places a percent sign (%) in the result. Does not require a corresponding value. Example: "Energy at %d%%." % 88 yields the value 'Energy at 88%.'.
"""
