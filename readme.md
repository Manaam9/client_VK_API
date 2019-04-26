# VK API script
Client to the VK API, which will consider the age distribution of friends
for the specified user. That is, the username or user_id of the user is input,
the output is a list of pairs (<age>, <number of friends with this age>),
sorted in descending order by the second key (number of friends) and in ascending
order by the first key (age). For example:
[(26, 8), (21, 6), (22, 6), (40, 2), (19, 1), (20, 1)]

You can run this script as a part of django preinstalled framework or
os stand-alone script.

How to run the script as stand alone:
1. Get access token for VK API
2. Get uid of target user
3. open friends.py and paste access token and uid in right places
3. run terminal
4. go to the current directory and run 'python friends.py'