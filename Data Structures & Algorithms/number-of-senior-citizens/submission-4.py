class Solution:
    def countSeniors(self, details: List[str]) -> int:
        #char 12-13 for each

        counter = 0
        for senior in details:
            if str(senior[11:13]).isdigit and int(str(senior[11:13])) > 60:
                counter += 1
        return counter