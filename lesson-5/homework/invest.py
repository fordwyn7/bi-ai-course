def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount += amount * rate / 100
        print(f"year {year}: ${"%.2f" % amount}")
amount, rate, years = map(int, input().split())
invest(amount, rate, years)