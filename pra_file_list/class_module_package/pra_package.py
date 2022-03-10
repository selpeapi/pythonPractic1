import pra_file_list.class_module_package.pra_module
from pra_file_list.class_module_package.pra_class import calculator2
from pra_file_list.class_module_package import pra_class

a =pra_file_list.class_module_package.pra_module
print(a.a)
# -> 111
pra_file_list.class_module_package.pra_module.a =222
print(pra_file_list.class_module_package.pra_module.a)
# -> 222

b =calculator2(1,2)
print(b.plus())
# -> 3

c =pra_class.lowCalculator(3,0)
print(c.divide())
# -> 0
