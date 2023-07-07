#This is recursive function for find palindrome words
def isPalindrome(theString):
    if len(theString) == 0 or len(theString) == 1:
        return True
    else:
        head = theString[0]
        middle = theString[1:-1]
        last = theString[-1]
        return head == last and isPalindrome(middle)


if __name__ == '__main__':
    text = 'racecar'
    print(text + ' is a palindrome: ' + str(isPalindrome(text)))
    text = 'amanaplanacanalpanama'
    print(text + ' is a palindrome: ' + str(isPalindrome(text)))
    text = 'tacocat'
    print(text + ' is a palindrome: ' + str(isPalindrome(text)))
    text = 'zophie'
    print(text + ' is a palindrome: ' + str(isPalindrome(text)))
