def weight_on_planets():
   # write your code here
   
   marsMult = 0.38
   jupMult = 2.34

   weight = input("What do you weigh on earth? ")

   weight = int(weight)

   print('\nOn Mars you would weigh', weight*marsMult, 'pounds.\nOn Jupiter you would weigh', weight*jupMult, 'pounds.')
   
if __name__ == '__main__':
   weight_on_planets()
