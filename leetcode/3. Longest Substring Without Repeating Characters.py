class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0   # 부분 문자열의 첫 문자의 index(초기값:0)
        dic = {}    # 문자들의 가장 마지막 위치의 인덱스를 담은 딕셔너리
        max_len = 0     # 나온 길이 중 최대 길이
        curr_len = 0    # 특정 문자 위치에서 가질 수 있는 최장 부분문자열의 길이
        for i, v in enumerate(s):
            if v not in dic:    # 처음 나오는 문자면 dic에 등록하고 현재 길이 1 증가
                dic[v] = i
                curr_len += 1
            else:   # 중복되는 문자가 나왔을 때
                if dic[v] >= start:     # 현재 부분문자열 내에 중복되는 문자가 포함
                    start = dic[v] + 1  # 시작 인덱스 변경
                    curr_len = i - dic[v]   # 변경된 현재 길이
                    dic[v] = i      # 중복된 문자의 마지막 위치 인덱스 갱신
                else:   # 현재 부분문자열 내에 포함되지 않아 영향이 없을 때
                    dic[v] = i
                    curr_len += 1
            
            if curr_len > max_len:
                max_len = curr_len
        
        return max_len
