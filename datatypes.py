# use integer
age = 13

# use string
customer_name = 'Aryan'

# use decimal
weight = 45.5

# use boolean
has_a_girlfriend = False


if age >= 18:
    print("Yes, u can vote")
else:
    print("Go to school")

if weight > 40 and age > 10:
    print("U can join Football team")
else:
    print("ur are malnutricious")


birth_year = 2006
current_year = 2006


while current_year <= 2050:
    new_age = current_year - birth_year
    print("{} was {} year old in {}".format(customer_name, new_age, current_year))
    current_year = current_year + 1


