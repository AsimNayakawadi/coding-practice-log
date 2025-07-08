# Problem : List Compression (HackerRank)
# Date: 2025-07-08
# Attempt 1
# Took ~1 hr. 
# Key learning: Range upper limit must be x+1 to include x
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l =([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)if n != i+j+k ])
    print(l)
