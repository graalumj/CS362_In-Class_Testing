# Word Count
# By: Jason Graalum
def count(str):
    return len(str.split())

if __name__ == '__main__':
    s = raw_input("Enter a string: ")
    
    print("Word Count: " + str(count(s)))

