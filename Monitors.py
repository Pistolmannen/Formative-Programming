from threading import Lock, Thread;
import threading;
import time;

class Guests(Thread):
  def __init__(self, Bowl):
    Thread.__init__(self)    # this is the important line
    self.Bowl = Bowl;
    # other standard class start up of your own here
       
  def run(self):
    # this method is where the process code goes. 

    time.sleep(0.5);
    Bowl.drink();
      
class Host(Thread):
  def __init__(self, Bowl):
    Thread.__init__(self)    # this is the important line
    self.Bowl = Bowl;
    # other standard class start up of your own here
       
  def run(self):
    # this method is where the process code goes. 
    for i in range(3):
      print("Hello World",i);
    # note that this is a limited process that will end, 
    # it does not have to be, or it might need an external signal

class BowlMonitor:
  def __init__(self, amount):
    self.monitor_lock=Lock();
    self.amount = amount;
	
  def drink(self):
    with self.monitor_lock:
        if self.amount > 0:
           self.amount -= 1;
           print("Driked");
            
            
      
Bowl = BowlMonitor(5);

Host = Host(Bowl);

Guest1 = Guests(Bowl);
Guest2 = Guests(Bowl);
Guest3 = Guests(Bowl);

Host.start();
Guest1.start();
Guest2.start();
Guest3.start();