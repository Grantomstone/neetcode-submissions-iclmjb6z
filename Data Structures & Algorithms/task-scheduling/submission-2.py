class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskMap = Counter(tasks)

        heap = [count for count in taskMap.values()]
        queue = deque([])
        heapq.heapify_max(heap)
        print(heap)

        count = 0
        while heap or queue:
            count += 1
            print(f"{heap=}\n{queue=}")
            
            if not heap:
                count = queue[0][1]
            else:
                cnt = heapq.heappop_max(heap) - 1
                if cnt:
                    queue.append((cnt, count + n))
            
            if queue and queue[0][1] == count:
                heapq.heappush_max(heap, queue.popleft()[0])
        return count