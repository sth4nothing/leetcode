from bisect import bisect
class Solution:
    def videoStitching(self, clips: 'List[List[int]]', T: int) -> int:
        clips.sort()
        if T == 0:
            return 0
        end = 0
        cnt = 0
        lidx, ridx = 
        while True:
            ridx = bisect(clips, [end + 1, 0], ridx + 1)
            if ridx - 1 < 0 or ridx - 1 >= len(clips):
                return -1
            ridx = min(clips[lidx:ridx])
            _, end = clips[ridx]
            cnt += 1
            if end >= T:
                return cnt



def main():
    s = Solution()
    print(s.videoStitching(
        [[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4], [4, 5], [5, 7], [6, 9]], 9))


main()
