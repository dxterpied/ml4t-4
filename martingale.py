"""Assess a betting strategy.  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		   	  			    		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		   	  			    		  		  		    	 		 		   		 		  
All Rights Reserved  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		   	  			    		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		   	  			    		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		   	  			    		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		   	  			    		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		   	  			    		  		  		    	 		 		   		 		  
or edited.  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		   	  			    		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		   	  			    		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		   	  			    		  		  		    	 		 		   		 		  
GT honor code violation.  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
Student Name: Yi Wang (replace with your name)  		   	  			    		  		  		    	 		 		   		 		  
GT User ID: ywang3404 (replace with your User ID)  		   	  			    		  		  		    	 		 		   		 		  
GT ID: 903389082 (replace with your GT ID)  		   	  			    		  		  		    	 		 		   		 		  
"""  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
import numpy as np  		   	  			    		  		  		    	 		 		   		 		  
import matplotlib.pyplot as plt
import pandas as pd		   	  			    		  		  		    	 		 		   		 		  
def author():  		   	  			    		  		  		    	 		 		   		 		  
        return 'ywang3404' # replace tb34 with your Georgia Tech username.  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
def gtid():  		   	  			    		  		  		    	 		 		   		 		  
	return 903389082 # replace with your GT ID number  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
def get_spin_result(win_prob=0.5):
    itera=0
    winnings=np.zeros(1000)
    episode_winnings =0
    while(episode_winnings<80 and itera<1000):
        won=False
        bet_amount=1
        while not won:
            if np.random.random() <= win_prob:
                won=True
            else:
                won=False
            if won==True:
                episode_winnings+=bet_amount
                winnings[itera]=episode_winnings
                itera+=1
                
            else:
                episode_winnings-=bet_amount
                winnings[itera]=episode_winnings
                bet_amount*=2
                itera+=1
    if episode_winnings>=80:
        winnings[itera-1:]=80
	  		   	  			    		  		  		    	 		 		   		 		  
	return winnings  		   	  			    		  		  		    	 		 		   		 		  
def get_spin_result2(win_prob):
    itera=0
    winnings=np.zeros(1000)
    episode_winnings =0
    while(episode_winnings<80 and itera<1000  and episode_winnings>-256  ):
        won=False
        bet_amount=1
        while not won:
            if np.random.random() <= win_prob:
                won=True
            else:
                won=False
            if won==True:
                episode_winnings+=bet_amount
                winnings[itera]=episode_winnings
                itera+=1               
            else:
                episode_winnings-=bet_amount
                winnings[itera]=episode_winnings
                if bet_amount*2>=episode_winnings+256:
                    bet_amount=episode_winnings+256
                else:
                    bet_amount*=2
                itera+=1
    if episode_winnings>=80:
        winnings[itera-1:]=80
    if episode_winnings<=-256:
       winnings[itera-1:]=-256
	  		   	  			    		  		  		    	 		 		   		 		  
    return winnings 
#print  	get_spin_result2(win_prob=0.6)	   	  			    		  		  		    	 		 		   		 		  
def test_code():  		   	  			    		  		  		    	 		 		   		 		  
    win_prob = 18.0/38 # set appropriately to the probability of a win  		   	  			    		  		  		    	 		 		   		 		  
    np.random.seed(gtid())
    # do this only once 
#experiment1 -1 		   	  		
    test_time=10
    result=np.zeros([test_time,1000])
    for i in range(test_time):
        result[i]=get_spin_result(win_prob)
    plt.figure(0)
    plt.xlabel('Iteration')
    plt.ylabel('Winnings')
    plt.xlim(0,300)
    plt.ylim(-256,100)
    plt.title('Figure 1')
    for i in range(test_time):
        plt.plot(pd.Series(result[i]))
    plt.savefig('Figure 1.png') 
     		  		  		    	 		 		   		 		  
    #return result # test the roulette spin  		   	  			    		  		  		    	 		 		   		 		  
#experiment1 -2    		   	  			    		  		  		    	 		 		   		 		  
	# add your code here to implement the experiments  		   	  			    		  		  		    	 		 		   		 		  
    test_time=1000
    result=np.zeros([test_time,1000])
    for i in range(test_time):
        result[i]=get_spin_result(win_prob)
    result_mean=np.mean(result,axis=0)	   
    result_std=np.std(result,axis=0)
    upper=result_mean+result_std	
    bottom=result_mean-result_std
    plt.figure(1)
    plt.xlabel('Iteration')
    plt.ylabel('Winnings')
    plt.xlim(0,300)
    plt.ylim(-256,100)
    plt.title('Figure 2')
    middle_line,=plt.plot(pd.Series(result_mean),label = 'Mean')
    upper_line,=plt.plot(pd.Series(upper),label = 'Upper')	
    bottom_line,=plt.plot(pd.Series(bottom),label = 'Bottom')	
    plt.legend(handles=[middle_line, upper_line,bottom_line], loc=4)	
    plt.savefig('Figure 2.png')	
    #plt.show()
#experiment1 -3    		   	  			    		  		  		    	 		 		   		 		  
	# add your code here to implement the experiments  		   	  			    		  		  		    	 		 		   		 		  
    test_time=1000
    result=np.zeros([test_time,1000])
    for i in range(test_time):
        result[i]=get_spin_result(win_prob)
    result_median=np.median(result,axis=0)	   
    result_std=np.std(result,axis=0)
    upper=result_median+result_std	
    bottom=result_median-result_std
    plt.figure(2)
    plt.xlabel('Iteration')
    plt.ylabel('Winnings')
    plt.xlim(0,300)
    plt.ylim(-256,100)
    plt.title('Figure 3')
    middle_line,=plt.plot(pd.Series(result_median),label = 'Median')
    upper_line,=plt.plot(pd.Series(upper),label = 'Upper')	
    bottom_line,=plt.plot(pd.Series(bottom),label = 'Bottom')	
    plt.legend(handles=[middle_line, upper_line,bottom_line], loc=4)	
    plt.savefig('Figure 3.png')	
    #plt.show()	 
#experiment2 -1  
    test_time=1000
    result=np.zeros([test_time,1000])
    for i in range(test_time):
        result[i]=get_spin_result2(win_prob)
    result_mean=np.mean(result,axis=0)	   
    result_std=np.std(result,axis=0)
    upper=result_mean+result_std	
    bottom=result_mean-result_std
    plt.figure(3)
    plt.xlabel('Iteration')
    plt.ylabel('Winnings')
    plt.xlim(0,300)
    plt.ylim(-256,100)
    plt.title('Figure 4')
    middle_line,=plt.plot(pd.Series(result_mean),label = 'Mean')
    upper_line,=plt.plot(pd.Series(upper),label = 'Upper')	
    bottom_line,=plt.plot(pd.Series(bottom),label = 'Bottom')	
    plt.legend(handles=[middle_line, upper_line,bottom_line], loc=4)
    plt.savefig('Figure 4.png')	   	
#experiment2 -2  
    test_time=1000
    result=np.zeros([test_time,1000])
    for i in range(test_time):
        result[i]=get_spin_result2(win_prob)
    result_median=np.median(result,axis=0)	   
    result_std=np.std(result,axis=0)
    upper=result_median+result_std	
    bottom=result_median-result_std
    plt.figure(4)
    plt.xlabel('Iteration')
    plt.ylabel('Winnings')
    plt.xlim(0,300)
    plt.ylim(-256,100)
    plt.title('Figure 5')
    middle_line,=plt.plot(pd.Series(result_median),label = 'Median')
    upper_line,=plt.plot(pd.Series(upper),label = 'Upper')	
    bottom_line,=plt.plot(pd.Series(bottom),label = 'Bottom')	
    plt.legend(handles=[middle_line, upper_line,bottom_line], loc=4)
    plt.savefig('Figure 5.png')		    		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		   	  			    		  		  		    	 		 		   		 		  
    test_code()  		   	  			    		  		  		    	 		 		   		 		  
