class Category:
  def __init__(self,name):
    self.name = name
    self.ledger = list()

  def check_funds(self,amount):
    fund = 0
    n=len(self.ledger)
    for i in range(n):
      fund += self.ledger[i]["amount"]
    if fund < amount:
      return False
    else:
      return True
  def deposit(self,amount,description=""):
    #initialising a dictionary
    self.depo = dict()
    #adding the amount and description to dictionary
    self.depo["amount"] = amount
    self.depo["description"] = description
    #adding the deposit to ledger list
    self.ledger.append(self.depo)

  def withdraw(self,amount,description="khilaf gatau buat apa"):
    #checking if total amount less than or greaten than amount to be withdrawn
    check = self.check_funds(amount)

    if(check == True):
      self.with_draw=dict()
      self.with_draw["amount"] = -(amount)
      self.with_draw["description"] = description
      self.ledger.append(self.with_draw)
      return True
    else:
      return False

  def get_balance(self):
    fund = 0
    n = len(food.ledger)
    #retrieving the total fund in ledger
    for i in range(n):
      fund += food.ledger[i]["amount"]
    return fund

  def transfer(self,amount,obname):
    objectname=obname.name
    give = self.withdraw(amount,f"Transfer to {objectname}")
    receive = obname.deposit(amount,f"Transfer from {self.name}")
    if(give == True):
      return True
    else:
      return False

  def check_funds(self,amount):
    fund = 0
    n = len(self.ledger)
    for i in range(n):
      fund += self.ledger[i]["amount"]
    if fund < amount:
      return False
    else:
      return True
  def __str__(self):
    title = f"{self.name:*^30}\n"
    items = ""
    total = 0
    for i in range(len(self.ledger)):
      items += f"{self.ledger[i]['description'][0:23]:23}{self.ledger[i]['amount']:>7.2f}\n"
      total += self.ledger[i]['amount']

    output = title + items + "Saldo: " + str(total)
    return output

  def separate_fund(self):
    note = 0
    for lis in self.ledger :
      if lis['amount'] < 0:
        note += lis['amount']
    return note

def spent(categories):
  money = 0
  note = []
  for category in categories :
    money += category.separate_fund()
    note.append(category.separate_fund())
  return note, money

def percent(categories):
  fund, sum = spent(categories)
  perc = []
  dot = []
  for i in fund :
    total_percent = int((i/sum) * 100.00)
    total_percent = int((total_percent - total_percent%10))
    perc.append(total_percent)
  for value in perc :
    dot.append(int(value/10))
  return perc, dot

def create_spend_chart(categories):
  total,num_bullet = percent(categories)
  a = 100
  disp = '\nPersentase pengeluaran\n'
  while a >= 0 :
    if a < 0 :
      break
    disp = disp + '          \n' + ' ' + str(a).rjust(3) + '|'
    for i in total :
      if a <= i :
        disp += ' o '
    a -= 10
  
  disp += '\n    ----------'
  names = []
  for i in categories :
    names.append(i.name)

  maks = max(names, key=len)
  name_str = ''
  for i in range(len(maks)) :
    name_str = name_str + '\n    '
    for j in names :
      if i >= len(j) :
        name_str = name_str + '   '
      else :
        name_str = name_str + '  ' + j[i]


  return disp + name_str