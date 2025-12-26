def largest_rectangle_area(heights):
    n = len(heights)
    max_area = 0

    for i in range(n):
        height = heights[i]

        # expand to left
        left = i
        while left >= 0 and heights[left] >= height:
            left -= 1

        # expand to right
        right = i
        while right < n and heights[right] >= height:
            right += 1

        width = right - left - 1
        area = height * width

        if area > max_area:
            max_area = area

    return max_area


# -------- User Input --------
n = int(input("Enter number of bars: "))

heights = []
for i in range(n):
    h = int(input(f"Enter height of bar {i+1}: "))
    heights.append(h)

result = largest_rectangle_area(heights)

print("Largest rectangle area:", result)
