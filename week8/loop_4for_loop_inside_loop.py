for i in range(10):
    print(i)
    for j in range(10):
        print(f"\t{j}")

# While we generally prefer variable names that are more descriptive than a single letter,
# if the variable will only be used for counting in a simple
# loop it is considered standard to use i. Then, if you have
# an inner loop, you use j, and a third inner loop would be k.
# If you have more than three loops you should consider if there is
# a simpler way to accomplish your task, and if there really isn't,
# you should at least move to more descriptive variable names at that point.
