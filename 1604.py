from typing import List
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        # create a hashmap that contains the times for each person
        # key is the persons name, value is an array of the persons key times
        # sort the key times for each person
        # iterate through the sorted times, if the two times are off by more than one hour, 
        # move to the next time, it is within an hour, check the next one is also within an hour
        # of the first time, if we find 3 then save the name to the response. 
        times = {}
        for name in keyName:
            if name not in times:
                times[name]=[]
        for i in range(len(keyName)):
            times[keyName[i]].append(keyTime[i])
        for key, value in times.items():
            value.sort();
        print(f'{times}')
        result = []
        for name, timesArray in times.items():
            print(f"name:{name}")
            for i in range(len(timesArray)):
                count = 1
                time1 = timesArray[i].split(':')
                print(f'time1 is {time1}')
                for j in range(i+1, len(timesArray)):
                    time2 = timesArray[j].split(':')
                    print(f'time2 is {time2}')
                    if int(time2[0])-int(time1[0]) == 0:
                        count+=1
                        if count == 3:
                            result.append(name)
                        continue
                    if int(time2[0])-int(time1[0]) == 1 and int(time2[1])-int(time1[1]) <= 0:
                        count+=1
                        if count == 3:
                            result.append(name)
                        continue
                    count=1
                    break

        uniqueNames = list(set(result)).sort()
        return  uniqueNames


keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"]
keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
# keyName = ["alice","alice","alice","bob","bob","bob","bob"]
# keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
s = Solution()
s.alertNames(keyName, keyTime)
