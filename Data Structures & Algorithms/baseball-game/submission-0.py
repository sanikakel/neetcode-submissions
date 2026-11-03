class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in operations:
            if i == "+":
                a = record[len(record)-1]
                b = record[len(record)-2]
                record.append(int(a) + int(b))
            elif i == "D":
                a = record[len(record)-1]
                record.append(2 * int(a))
            elif i == "C":
                record.pop()
            else:
                record.append(int(i))
    
        return sum(record)