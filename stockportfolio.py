# # STOCK PORTFOLIO TRACKER

stocks = {"META":485, "NFLX":628, "NVDA":875, "UBER":63, "SONY":90}

def get_int(msg):
    while True:
        try:
            x = int(input(msg))
            return x if x > 0 else print("Enter positive number")
        except:
            print("Invalid input")

print("="*40, "\n STOCK PORTFOLIO TRACKER\n", "="*40)

for s, p in stocks.items():
    print(f"{s}: ${p}")

n = get_int("\nHow many stocks? ")

portfolio, total = [], 0

for i in range(n):
    s = input("\nStock: ").upper()
    if s not in stocks:
        print("Invalid stock")
        continue

    q = get_int("Quantity: ")
    val = stocks[s] * q
    total += val
    portfolio.append((s, q, val))

print("\nSUMMARY\n" + "-"*30)

for s, q, v in portfolio:
    print(f"{s} | {q} shares | ${v} | {v/total*100:.2f}%")

print("\nTotal:", total)

with open("portfolio.txt", "w") as f:
    for s, q, v in portfolio:
        f.write(f"{s} {q} {v} {v/total*100:.2f}%\n")
    f.write(f"\nTotal: {total}")