num_people_show1 = int(input())
rating_show1 = float(input())
num_people_show2 = int(input())
rating_show2 = float(input())
num_people_show3 = int(input())
rating_show3 = float(input())
weighted_sum = (num_people_show1 * rating_show1) + (num_people_show2 * rating_show2) + (num_people_show3 * rating_show3)
total_people = num_people_show1 + num_people_show2 + num_people_show3
average_rating = weighted_sum / total_people
rounded_rating = round(average_rating, 2)
print(rounded_rating)
