'''
+ 15:35 ~ 16:37
시작 시각 : 22:51
종료 시각 : 23:48
'''


class Cake:
    def __init__(self, name, price, ingredient):
        self.name=name
        self.price=price
        self.ingredient=ingredient


class Shop:
    def __init__(self):
        self.ingredient={}
        self.product={}
        
    def buy_ingredient(self, ingredient):
        a=list(self.keys())
        b=list(self.values())
        for i in range (0,len(a)-1):
            if a[i] in self:
                self.ingredient[a[i]]+=b[i]
            else:
                self.ingredient[a[i]]=b[i]
        global inventory
        inventory=self.ingredient
        return self.ingredient
            
            
    def current_ingredient(self):
        c=list(self.ingredient.keys())
        d=list(self.ingredient.values())
        for j in range (0,len(c)-1):
            if d[i]=0:
                remove(d[i])
                remove(c[i])
                j-=1
        k="현재 보유한 재료는 "
        print(k)
        for i in range (0,len(c)-1):
            if i=len(c)-1:
                print(c[i],"(",d[i],"개)입니다.")
            else:
                print(c[i],"(",d[i],"개), ")
        

    def make_cake(self):
        e=list(self.ingredient.keys())
        f=list(self.ingredient.values())
        x=0
        for i in range (0,len(e)-1):
            if (e[i] in inventory) and (f[i] in inventory) and (f[i]-inventory[e[i]]>=0):
        pass


class Pos:
    def __init__(self, cake_shop):
        pass

    def current_cakes(self):
        pass

    def sell_cake(self, cakename):
        pass

    def print_current_money(self):
        pass


cheesecake = Cake("Cheese Cake", 6900, {'cheese': 2, 'egg': 2, 'butter': 2})
chococake = Cake("Chocolate Cake", 5900, {'chocolate': 2, 'egg': 2, 'butter': 2})
carrotcake = Cake("Carrot Cake", 5500, {'carrot': 2, 'walnut': 2, 'egg': 1, 'butter': 1})
creamcake = Cake("Fresh Cream Cake", 4500, {'cream': 3, 'egg': 1, 'butter': 1})
swpotatocake = Cake("Sweet Potato Cake", 6500, {'sweet potato': 3, 'egg': 2, 'butter': 1})

cake_shop = Shop()
cake_shop.buy_ingredient({'cheese': 5, 'carrot': 3, 'sweet potato': 3, 'egg': 10, 'butter': 10})
cake_shop.current_ingredient()
cake_shop.buy_ingredient({'chocolate': 3, 'walnut': 2, 'egg': 12, 'butter': 12})
cake_shop.current_ingredient()

print("\nMAKE CAKE")
cake_shop.make_cake(creamcake)
print(cake_shop.ingredient)
cake_shop.make_cake(carrotcake)
print(cake_shop.ingredient)
cake_shop.make_cake(carrotcake)
print(cake_shop.ingredient)
cake_shop.make_cake(cheesecake)
print(cake_shop.ingredient)
cake_shop.make_cake(cheesecake)
print(cake_shop.ingredient)
cake_shop.make_cake(chococake)
print(cake_shop.ingredient)
cake_shop.make_cake(swpotatocake)
print(cake_shop.ingredient)
cake_shop.current_ingredient()

pos = Pos(cake_shop)
print()
pos.current_cakes()

print()
pos.sell_cake('Cheese Cake')
pos.current_cakes()

print()
pos.sell_cake('Cheese Cake')
pos.current_cakes()

print()
pos.sell_cake('Chocolate Cake')
pos.current_cakes()

print()
pos.sell_cake('Cheese Cake')

print()
pos.print_current_money()
