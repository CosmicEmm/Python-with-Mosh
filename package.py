#importing the entire module: prefix the module name with the name of its package
import ecommerce.shipping
ecommerce.shipping.calc_shipping()

#importing a specific function from the module
from ecommerce.shipping import calc_shipping
calc_shipping()

#alterative approach
from ecommerce import shipping
shipping.calc_shipping()

