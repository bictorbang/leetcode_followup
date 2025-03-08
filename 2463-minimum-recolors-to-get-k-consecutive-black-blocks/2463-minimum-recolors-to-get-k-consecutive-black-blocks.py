class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_w = 100
        for i in range(len(blocks) - k + 1):
            cur_w = sum(1 for x in blocks[i:i+k] if x == "W")
            min_w = min(cur_w, min_w)
        return min_w
