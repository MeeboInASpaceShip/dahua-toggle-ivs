# dahua-toggle-ivs
Python scripts to toggle Dahua IVS rules on or off

Currently there are two scripts since I've been too lazy to get command line options and merge them into one.
If somebody would care to take the 15 minutes to do this, it would be much appreciated.

Note: these are crude scripts that gets the basic job done. There is no error checking or other fancy
functionality such as configurable IP addresses, usernames, passwords and so forth. You are free to pull,
improve and I'll happily merge!

There are some commented out print() statements that you may enable for debugging purposes.

Make sure to change ruleNameList (line 13), the camera's IP address (line 17 and 41) and API username/password
(line 22 and 46, normally the camera's "admin" account and password)
