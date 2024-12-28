import heapq

def product_of_three_largest(nums):
    if len(nums) < 3:
        raise ValueError("The input list must have at least three distinct elements.")

    # Use a set to ensure distinct elements
    distinct_nums = list(set(nums))

    if len(distinct_nums) < 3:
        raise ValueError("The input list must have at least three distinct elements after removing duplicates.")

    # Use a min-heap to find the three largest distinct elements
    # A heap of size 3 will store the largest 3 elements as we iterate through the list
    heap = []
    for num in distinct_nums:
        heapq.heappush(heap, num)  # Push the element into the heap
        if len(heap) > 3:
            heapq.heappop(heap)  # Ensure the heap size is at most 3
    
    # The heap now contains the three largest distinct elements
    largest_three = heap

    # Compute the product of these three elements
    product = 1
    for num in largest_three:
        product *= num

    return product

# Example usage
nums = [10, 20, 30, 5, 20, 10]
try:
    result = product_of_three_largest(nums)
    print("The product of the three largest distinct elements is:", result)
except ValueError as e:
    print(e)
