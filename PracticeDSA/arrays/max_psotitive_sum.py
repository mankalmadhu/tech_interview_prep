# https://www.interviewbit.com/problems/max-non-negative-subarray/
class Solution:
    # @param A : list of integers
    # @return a list of integers
    
    def maxset(self, A):
        max_sum = -1
        cur_sum = 0
        reset_index = 0
        best_start = 0
        best_end = 0
        
        for idx,i in enumerate(A):
            if i < 0:
                cur_sum = 0 
                reset_index = idx+1
                continue
            
            cur_sum += i
            
            if cur_sum > max_sum:
                max_sum = cur_sum
                best_start = reset_index
                best_end = idx
            if cur_sum == max_sum:
                cur_sub_arr_len = idx-reset_index
                best_sub_arr_len = best_end - best_start
                if (cur_sub_arr_len > best_sub_arr_len) or ((cur_sub_arr_len == best_sub_arr_len) and (reset_index < best_start)):
                    best_start = reset_index
                    best_end = idx
        
        if max_sum == -1:
            return []
        
        return A[best_start:best_end+1]
            
                
        
    def maxset1(self, A):
        
        max_sum = 0
        cur_sum = 0
        start_to_end_index_tuple_list = []
        reset_index = 0
        
        for i in range(len(A)):
            if A[i] < 0:
                cur_sum = 0 
                reset_index = i+1
                continue
                
            cur_sum += A[i]
            
            if cur_sum > max_sum:
                start_to_end_index_tuple_list = [(reset_index, i)]
                max_sum = cur_sum
            if cur_sum == max_sum:
                start_to_end_index_tuple_list.append((reset_index, i))
                
        if not start_to_end_index_tuple_list:
            return []      
        if len(start_to_end_index_tuple_list)>1:
            sorted_list = sorted(start_to_end_index_tuple_list, key=lambda x: (x[0] - x[1], x[0]))      
            result = sorted_list[0]
        else:
            result = start_to_end_index_tuple_list[0]
        
        return A[result[0]: result[1]+1]
                                    
