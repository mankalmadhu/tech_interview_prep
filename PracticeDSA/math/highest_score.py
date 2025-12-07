#https://www.interviewbit.com/problems/highest-score/
class Solution:
    def highestScore(self, A):
        student_scores = {}
        
        for marks in A:
            student = marks[0]
            score = int(marks[1])
            
            if student in student_scores:
                student_scores[student].append(score)
            else:
                student_scores[student] = [score]
        
        # Calculate averages
        averages = []
        for scores in student_scores.values():
            avg = sum(scores) / len(scores)
            averages.append(avg)
        
        # Return the highest average
        return int(max(averages))