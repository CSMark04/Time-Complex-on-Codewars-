
#https://www.codewars.com/kata/5266876b8f4bf2da9b000362
def likes(names):
# Time Complexity O(n + 4) > O(n)
    likes = []
    for name in names: # O(n)
        likes.append(name)
        
    if len(likes) >= 4:  #O(1)
        number = len(likes) - 2
        return f'{likes[0]}, {likes[1]} and {number} others like this'
    elif len(likes) == 3: #O(1)
        return f'{likes[0]}, {likes[1]} and {likes[2]} like this'
    elif len(likes) == 2: #O(1)
        return f'{likes[0]} and {likes[1]} like this'
    elif len(likes) == 1: #O(1)
        return f'{likes[0]} likes this'
    else:
        return 'no one likes this'


#https://www.codewars.com/kata/526dbd6c8c0eb53254000110
# time complexity is O(n), the built in method .isalnum is probably looping through the passwords and checking it.  
def alphanumeric(password):
    return password.isalnum()



# https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/python
#time complexity is O(n) since we are looping
def reverse_words(s):
    splitStr = s.split()[::-1]
    st = []
    for word in splitStr:
        st.append(word)
    return ' '.join(st)