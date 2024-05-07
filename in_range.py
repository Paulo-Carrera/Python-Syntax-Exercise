def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """

    for num in nums:
        if num in range(lowest,highest + 1):
            print( f"{num} fits")

print("example1:")
in_range([10, 20, 30, 40, 50], 15, 30)

print("example2:")            
in_range([1,2,3,4,5,6,7,8,9,10], 4,9)