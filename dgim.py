import collections

class DGIM:
    def __init__(self, window_size):
        self.window_size = window_size
        self.buckets = collections.defaultdict(list) # Stores buckets by their size (power of 2)
        self.current_time = 0

    def add_bit(self, bit):
        self.current_time += 1
        # Remove expired buckets
        for size in list(self.buckets.keys()):
            for i, bucket in enumerate(self.buckets[size]):
                if bucket['end_time'] < self.current_time - self.window_size:
                    self.buckets[size].pop(i)
                else:
                    break # Buckets are ordered by time, so no need to check further

        if bit == 1:
            # Create a new bucket of size 1 (2^0) for the new '1' bit
            new_bucket = {'size': 1, 'end_time': self.current_time}
            self.buckets[1].append(new_bucket)

            # Merge buckets if there are more than two of the same size
            size_to_check = 1
            while len(self.buckets[size_to_check]) > 2:
                # Merge the two oldest buckets of this size
                bucket1 = self.buckets[size_to_check].pop(0)
                bucket2 = self.buckets[size_to_check].pop(0)
                
                merged_bucket_size = size_to_check * 2
                merged_bucket_end_time = bucket2['end_time'] # Use the end_time of the newer bucket
                
                merged_bucket = {'size': merged_bucket_size, 'end_time': merged_bucket_end_time}
                self.buckets[merged_bucket_size].append(merged_bucket)
                size_to_check = merged_bucket_size

    def estimate_ones(self):
        count = 0
        latest_bucket_time = 0
        
        # Find the latest bucket within the window
        for size in sorted(self.buckets.keys(), reverse=True):
            if self.buckets[size]:
                # The latest bucket of any size is the rightmost one
                latest_bucket = self.buckets[size][-1] 
                if latest_bucket['end_time'] >= self.current_time - self.window_size:
                    latest_bucket_time = max(latest_bucket_time, latest_bucket['end_time'])

        # Sum up the sizes of buckets within the window,
        # treating the oldest bucket within the window as having half its size
        for size in sorted(self.buckets.keys(), reverse=True):
            for bucket in self.buckets[size]:
                if bucket['end_time'] >= self.current_time - self.window_size:
                    if bucket['end_time'] == latest_bucket_time and len(self.buckets[size]) == 1:
                        # If it's the latest bucket and the only one of its size, count full size
                        count += bucket['size']
                    else:
                        # Otherwise, count full size
                        count += bucket['size']
                elif bucket['end_time'] < self.current_time - self.window_size and \
                     bucket['end_time'] > self.current_time - self.window_size - bucket['size']:
                    # If partially within window, approximate as half
                    count += bucket['size'] / 2
        return int(count)

# Example Usage:
if __name__ == "__main__":
    window_size = 10
    dgim_algo = DGIM(window_size)
    
    stream = [ 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1]
    
    for bit in stream:
        dgim_algo.add_bit(bit)
        print(f"Added bit: {bit}, Current estimate of 1s in window: {dgim_algo.estimate_ones()}")