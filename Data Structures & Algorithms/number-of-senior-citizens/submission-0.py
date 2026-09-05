class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniors = 0
        for d in details:
            if int(d[11:13]) > 60:
                seniors += 1
        return seniors