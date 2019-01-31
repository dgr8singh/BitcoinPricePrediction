from pickle import dump, load
import  random
from datetime import  date
l = [1,2]
dbfile = open('p.pkl', "wb")
print(dbfile)
dump(l, dbfile)
dbfile.close()

z = load(open('p.pkl', 'rb'))
if z[1] == 1:
   f=0
else:
   f=1

def g():
   if f:
      print("x")
   else:
      print("y")

if __name__ == "__main__":
   past_actual=[1,2,3]
   past_actual = past_actual[::-1]
   data = []
   data.append([round(past_actual[0] + random.uniform(10, 15), 2)])
   data[0].append(round(data[0][0] + random.uniform(10, 15), 2))
   data[0].append(round(data[0][1] + random.uniform(10, 15), 2))
   data.append([round(past_actual[0] + random.uniform(10, 15), 2), round(past_actual[1] + random.uniform(10, 15), 2),
                round(past_actual[2] + random.uniform(10, 15), 2)])
   data.append([past_actual[0], past_actual[1], past_actual[2]])
   dump(data, open("p.pkl", "wb"))

