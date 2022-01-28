
#comparing 2 arrays to one another inspired by algorithm on longest common substring problem
def compare2ars(byte_arr_one, byte_arr_two):

    #create a double array and fill with the count of recurrance if bytes are the same
    freq = [[0 for i in range(len(byte_arr_one) + 1)] for i in range(len(byte_arr_two) + 1)]
    
    # iterate through both arrays
    for i in range(len(byte_arr_one) - 1, -1, -1):
        for j in range(len(byte_arr_two) - 1, -1, -1):
 
            if byte_arr_one[i] == byte_arr_two[j]:
                freq[j][i] = freq[j + 1][i + 1] + 1
    max_freq = 0
    
    x = -1
    y = -1
    # find max location

    for i in range(len(freq)):
        for j in range(len(freq[i])):
            
            if (freq[i][j] > max_freq):
                x = i
                y = j
                max_freq= freq[i][j]

    common_subarr = []
    while (x >= 0 and x < len(freq) and y < len(freq[x]) and freq[x][y] > 0):
        common_subarr.append(byte_arr_one[y])
        x += 1
        y += 1
    freq.clear()

    #return common longest subarr
    return common_subarr

#find the longest strand and return specific information per file
def longestStrand(files):
    # a list of byte arrays
    byte_arr = []

    #the longest array
    longest_arr = []


    files_with_subarr = []
    #for every byte find the 

    #open every file in list
    for i in files:
        iFile = open(i, "rb")
        i_byte = iFile.read()
        i_byte_arr = [i_byte[j: j+1] for j in range(len(i_byte))]
        byte_arr.append(i_byte_arr)

    # compare every file with one another to find longest strand
    for i in range(0, len(files) - 1):
        for j in range(i + 1, len(files)):
            temp = compare2ars(byte_arr[i], byte_arr[j])
            if (len(temp) > len(longest_arr)):
                longest_arr = temp
    
    # add files and offset number that contain longest strand
    for i in range(0, len(files)):
        # if i not in files_with_subarr:
            curr = byte_arr[i]
            for j in range(len(curr)- len(longest_arr) + 1):
                if longest_arr == curr[j: j+len(longest_arr)]:
                    files_with_subarr.append( (files[i],j))
    

    return longest_arr, files_with_subarr

    
Longest_Strand, files_w_offset = longestStrand(["Eluvio Challenge - Core Engineering\sample.1", "Eluvio Challenge - Core Engineering\sample.2", "Eluvio Challenge - Core Engineering\sample.3", "Eluvio Challenge - Core Engineering\sample.4", "Eluvio Challenge - Core Engineering\sample.5", "Eluvio Challenge - Core Engineering\sample.6", "Eluvio Challenge - Core Engineering\sample.7", "Eluvio Challenge - Core Engineering\sample.8", "Eluvio Challenge - Core Engineering\sample.9", "Eluvio Challenge - Core Engineering\sample.10" ])

# Longest_Strand, files_w_offset = longestStrand(["Eluvio Challenge - Core Engineering\sample.1", "Eluvio Challenge - Core Engineering\sample.2", "Eluvio Challenge - Core Engineering\sample.3"])
print(Longest_Strand)
print(files_w_offset)