def minimum_points(threshold, points):
    # write your code here
    total = 0
    num_questions = 0
    #count += points[0]
    for point in points:
        total += point
        first_point = points[0]
        if total > (threshold + first_point):
            break
        num_questions += 1
    return num_questions


if __name__ == "__main__":
    # write your debug code here
    print(minimum_points(2, [1, 2, 3]))
    print(minimum_points(4, [1, 2, 3, 4, 5]))
    print(minimum_points(4, [1, 2, 3, 5, 8]))
    print(minimum_points(12, [1, 2, 3, 5, 8, 13, 14, 15, 18]))
    print(minimum_points(100, [1]))
