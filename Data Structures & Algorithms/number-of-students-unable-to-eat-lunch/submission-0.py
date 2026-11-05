class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # 0 = circular, 1 = square
        # len(students) = len(sandwiches)
        # students = queue
        # sandwiches = stack
        # if students[front] == sandwiches[top]: students.dequeue(), sandwiches.pop()
        # else: x = students[front] students.dequeue(), students.enqueue(x)
        # continue while sandwiches[top] != all([s for s in students])
        # return len(students) after exiting loop
        # sandwiches[0] is the sandwich on top of stack
        # students[0] is the student at front of the queue

         
        i, j = 0, 0
        c = 0
        while c < len(sandwiches) and i < len(sandwiches):
            if sandwiches[i] == students[j]:
                c = 0
                i += 1
                j += 1
            else:
                c += 1
                students.append(students[j])
                j += 1

        return len(sandwiches) - i
