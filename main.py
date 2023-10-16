
import matplotlib.pyplot as plt
import numpy as np


dataset = [[1,1] , [1,-1] , [-1,1] , [-1,-1]]
input = [[1,1],[-1,1],[2,1],[1,-6],[3,2],[-1,-4],[-2,3],[-1,-1],[5,-4],[-1,-3]]
output = [1,-1,-1,-1]
initial_weight = [0,0,0]
    

def learn():
    
    for i in range(len(dataset)): 
        delta_bias = output[i]
        delta_weight1 = (dataset[i][0] * output[i])
        delta_weight2 = (dataset[i][1] * output[i])
        initial_weight[0] = initial_weight[0] + delta_bias
        initial_weight[1] = initial_weight[1] + delta_weight1
        initial_weight[2] = initial_weight[2] + delta_weight2
    print(initial_weight)    

     
def test(test_input):
    
    y = []
    for i in test_input :
        if initial_weight[0] + (i[0]*initial_weight[1]) + (i[1]*initial_weight[2]) >= 0 :
            y.append(1)
        else :
            y.append(-1)
        
    print(y)    
        
   


def draw(initial_weight ,input):
    
    x1_scatter = np.linspace(-10, 10, 100)
    x2_scatter = np.linspace(-10, 10, 100) 
    var1_grid, var2_grid = np.meshgrid(x1_scatter, x2_scatter)
    y = initial_weight[0] + initial_weight[1] * var1_grid + initial_weight[2] * var2_grid
    
    plt.contour(x1_scatter , x2_scatter , y , levels=[0] , colors='g')
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    
    for i in input :
        if (initial_weight[0] + initial_weight[1] * i[0] + initial_weight[2] * i[1]) > 0:
            plt.scatter(i[0], i[1], color='green', label='x1, x2')
        else:
            plt.scatter(i[0], i[1], color='red', label='x1, x2')



    plt.legend()
    plt.show()




learn()
test(input)

draw(initial_weight , input)

    
       
        
