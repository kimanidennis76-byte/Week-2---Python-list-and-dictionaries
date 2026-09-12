# Day 2
step_counts = [8800, 6500, 11000, 9200, 7300,8800]

step_counts.append(10500)
step_counts.remove(6500)
step_counts.sort(reverse=True)

print("Final steps:",step_counts)


high_days = 0
for s in step_counts:
  if s >= 9000:
    
    high_days += 1
print("Days over 9000 steps:", high_days)


