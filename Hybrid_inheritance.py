## Hybrid Inheritance 
# A combination of single and multiple inheritance 
 
class BaseClass:
    pass 

class DerivedClass1(BaseClass):
    pass

class DerivedClass2(BaseClass):
    pass

class DerivedClass3(DerivedClass1, DerivedClass2):
    pass

## Hierarchical Inheritance 

class BaseClass:
    pass

class D1(BaseClass):
    pass

class D2(BaseClass):
    pass
 
class D3(D1):
    pass

class D4(D2):
    pass
