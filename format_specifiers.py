# format specifiers = {:flags} format a  value based on what flags are inserted

# .(number)f = round to that many decimal palces (fixed point)
# :(number) =allocate that many spaces
# :03 = allocate and zero pad that many spaces 
# :< = left justify
# :> = right justify
# :^ = center justify
# :+ = use plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"price 1 is ${price1:+}")
print(f"price 2 is ${price2:,}")
print(f"price 3 is ${price3:+,.2f}")