# cafe-review
a simple machine learning example to predict reviews

the tricky part of the data is the "Cuisine" attribute
it contains multiple attributes, separated by "comma"

using one hot encoding could be too long ~ 80 characters
so, it's good to break the coded cuisine into 4 parts.

how?
cuisine is decomposed into country and aux
country = Turkish, Middle eastern etc
aux = Deli, Street Food

example?
Cuisine : Italian, Steakhouse, Barbecue
Country : Italian
Aux     : Steakhouse, Barbecua
