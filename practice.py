def processcase(case_num):
    # read input fo each single case
    (num_candy_bags, num_kids) = tuple(map(int, input().split()))
    candy_counts = list(map(int, input().split()))
    #compute the total amount of candy
    total_candy = 0
    for i in range(num_candy_bags):
        total_candy += candy_counts[i]
    #use module to calculate remaining candy
    amount_remaining = total_candy % num_kids

    print(f"Case #{case_num}: {amount_remaining}")

#iterate through each case
num_cases = int(input())
for i in range(num_cases):
    processcase(i+1)