from threading import Thread;
import threading;
import time;
import math;




# Chopsticks
Chopstick1 = threading.Semaphore(value=1);
Chopstick2 = threading.Semaphore(value=1);
Chopstick3 = threading.Semaphore(value=1);
Chopstick4 = threading.Semaphore(value=1);
Chopstick5 = threading.Semaphore(value=1);

Chopsticks = [Chopstick1, Chopstick2, Chopstick3, Chopstick4, Chopstick5];



class Philosopher(Thread):
  def __init__(self,id,cuttlery,l):
    Thread.__init__(self);    # this is the important line
    # other standard class start up of your own here
    self.id=id;
    self.cuttlery=cuttlery;
    self.loglist=l
       
  def run(self):
    # this method is where the process code goes. 

    for _ in range(10):
        time.sleep(2);
        if 1 == (self.id % 2):
            self.cuttlery[(self.id-1) % 5].acquire();
            time.sleep(0.1);
            self.loglist.append((self.id, " have picked up: ", (self.id-1) % 5))
            
            self.cuttlery[self.id].acquire();
            time.sleep(0.1);
            self.loglist.append((self.id, " have picked up the other: ", self.id))

            print("hello ",self.id);
            time.sleep(0.3);
        
            self.cuttlery[self.id].release();
            time.sleep(0.1);
            self.loglist.append((self.id, " have put down: ", self.id))
            self.cuttlery[(self.id-1) % 5].release();
            time.sleep(0.1);
            self.loglist.append((self.id, " have put down the other: ", (self.id+1) % 5))
        else:
           
            self.cuttlery[self.id].acquire();
            time.sleep(0.1);
            self.loglist.append((self.id, " have picked up: ", self.id))
            self.cuttlery[(self.id+1) % 5].acquire();
            time.sleep(0.1);
            self.loglist.append((self.id, " have picked up the other: ", (self.id+1) % 5))

            print("hello ",self.id);
            time.sleep(0.3);

            self.cuttlery[self.id].release();
            time.sleep(0.1);
            self.loglist.append((self.id, " have put down: ", self.id))
            self.cuttlery[(self.id+1) % 5].release();
            time.sleep(0.1);
            self.loglist.append((self.id, " have put down the other: ", (self.id+1) % 5))
    # note that this is a limited process that will end, 
    # it does not have to be, or it might need an external signal


localLog=[]

# Philosophers
Philosopher1 = Philosopher(0,Chopsticks,localLog);
Philosopher2 = Philosopher(1,Chopsticks,localLog);
Philosopher3 = Philosopher(2,Chopsticks,localLog);
Philosopher4 = Philosopher(3,Chopsticks,localLog);
Philosopher5 = Philosopher(4,Chopsticks,localLog);

Philosopher1.start();
Philosopher2.start();
Philosopher3.start();
Philosopher4.start();
Philosopher5.start();

Philosopher1.join();
Philosopher2.join();
Philosopher3.join();
Philosopher4.join();
Philosopher5.join();

for x in localLog:
   print(x)

'''
myLock=threading.Lock(); # makes a lock object
myLock.acquire(); # block here until I have control 
# do my thing 
myLock.release(); # let it go, if other threads are waiting 
                 # someone will get control
'''

