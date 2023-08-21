discount = .15
salesTax = .10
def discountedPrice(price):
    discountedPrice = price - (discount * price) + (price * salesTax)
    print("Original Cost:", price, "Discounted Price:",round(discountedPrice, 2))
    return discountedPrice

discountedPrice(299.12)
discountedPrice(28283.213)
discountedPrice(22324)
discountedPrice(12)
discountedPrice(39.99)