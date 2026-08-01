class Solution:
    def CompressionAlgorithm(self,char:list[str])->int:
        read = 0 
        write = 0
        while read<len(char):
            j = read 
            while j < len(char) and char[j]==char[read]:
                j+=1

            count = j-read

            char[write]=char[read]
            write+=1

            if count > 1:

                for digit in str(count):
                    char[write]=digit
                    write+=1
            read = j 

        return write 


obj = Solution()
char = ["a","a","b","b","b","c","c","c","c"]
print(obj.CompressionAlgorithm(char))