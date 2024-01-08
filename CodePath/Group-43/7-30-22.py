'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Examples:

Input:
[[11110],
[11010],
[11000],
[00000]]

Output:  1

Input:
11000
11000
00100
00011

Output: 3
'''


def numberislands(matrix):
    island = 0

    def bfs(matrix, i, j):
        print("in bfs")
        if j + 1 < len(matrix[0]):
            print("in j+1")
            if matrix[i][j + 1] == '1':
                matrix[i][j + 1] = '0'
                bfs(matrix, i, j + 1)

        if j - 1 > 0:
            print("in j-1")
            if matrix[i][j - 1] == '1':
                matrix[i][j - 1] = '0'
                bfs(matrix, i, j - 1)

        if i + 1 < len(matrix):
            print("in i+1")
            if matrix[i + 1][j] == '1':
                matrix[i + 1][j] = '0'
                bfs(matrix, i + 1, j)

        if i - 1 > 0:
            print("in i-1")
            if matrix[i - 1][j] == '1':
                matrix[i - 1][j] = '0'
                bfs(matrix, i - 1, j)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("looping")
            if matrix[i][j] == '1':
                print("hit a 1")
                island += 1
                matrix[i][j] = '0'
                bfs(matrix, i, j)

    return island


print(
    numberislands([['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'],
                   ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]))

print(
    numberislands([['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'],
                   ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]))
