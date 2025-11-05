class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            words = log.split(" ")
            l = len(words)
            count = l-1
            for i in range(1,l):
                if words[i].isdigit():
                    #print("words[i]", words[i])
                    count -= 1
            #print("l", l,"count", count,"words", words)
            if count == 0:
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        #print("letter_logs", letter_logs)
        letter_logs = sorted(letter_logs, key=lambda x: (' '.join(x.split(" ")[1:]) , x.split(" ")[0] ))
        letter_logs.extend(digit_logs)
        return letter_logs
