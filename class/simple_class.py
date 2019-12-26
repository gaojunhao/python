class father:
    a = 1
    def func(self):
        return 'father function'

instance = father()

print('instance a: %d' %(instance.a))
print('instance func:', instance.func())
