# Create three different variables. The first variable should use all
# lower case characters with underscore ( _ ) as the word separator.
# The second variable should use all upper case characters with
# underscore as the word separator. The third variable should use numbers,
# letters, and underscore, but still be a valid variable Python variable name.
# Make all three variables be strings that refer to IPv6 addresses.
# Use the from future technique so that any string literals in Python2 are unicode.

from __future__ import unicode_literals

multicast_solicited_node = u'FF02::1:FF00:0000/104'

LINK_LOCAL = u'FE80::/10'

embedded_ipv4 = u'::/80'

# compare if variable1 equals variable2
print(multicast_solicited_node == LINK_LOCAL)

# compare if variable1 is not equal to variable3
print(multicast_solicited_node != embedded_ipv4)