# RA
Dual-class stocks data processing.
## 1. Questions 
### 1.1 Option
Call option holders are not entitled to regular quarterly dividends. So when I compute the cash-flow rights with the 
numbers from DEF-14A "Security Ownership of Certain Beneficial Owners and Management" shall I 
subtract those shares of common stock included in the above form which may be acquired upon the exercise of options that 
are exercisable?

## 2. Companies Status Not Determined yet
### 28917 D
Class A Common Stock are empowered as a class to elect one-third of the Directors and the holders of Class B Common Stock
 are empowered as a class to elect two-thirds of the Directors.


### 30419
Common stock & Preferred stock(42.15 votes per share)  
No dividend paid for common stock.

### 33113
Only on liquidation could the preferred stock shareholder receive the dividends.

### 39648 G&K SERVICES INC
Conversed all Class B shares to Class A shares in 2005.

### 43196 GRAY TELEVISION INC
Assumes equal dividends as before 2008.

### 43920
More than 2003-2007 as in the raw excel.  

### 46640
Little preferred stock.

### 49401
2004 Special cash dividend?  
Commencing with the quarterly dividend declared on February 17, 2004, the Board of Directors increased the regular 
quarterly dividend on our Class A Common Stock to $0.050 per share and the regular quarterly dividend on our Class B 
Common Stock to $0.055 per share. Following the dividends declared on February 17, 2004, the Board of Directors declared 
regular quarterly dividends in 2004 on May 19, 2004, August 2, 2004 and November 4, 2004, each in the amount announced 
on February 17, 2004. Also, on February 17, 2004, our Board of Directors declared a special cash dividend of $4.00 per 
share on each of our Class A Common Stock and Class B Common Stock. 

### 50471 
Don't know the per share dividend of preferred stock and the common stock has never paid dividends.

### 52532
Common stock and preferred stock. One vote for each share. No dividend data in 10-K of both types of stock.

## 2. Process Method
### 2.1 Description


### 2.2 Voting Example
#### 2.2.1 1611988 Fifth Street Asset Management Inc. 2015-04-23
|SHAOUTA|SHAOUTB|VOTEA|VOTEB|CLASSANUM|CLASSAPCT|CLASSBNUM|CLASSBPCT|VOTEPCT|
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
|6,000,033 |42,856,854|1|5|184,283|3.10|42,854,854|100.00|97.35|  


The method of computing voting rights using now
: ![equ](https://latex.codecogs.com/gif.latex?\frac{ClassAnum*VoteA&plus;ClassBnum*VoteB}{ClassAnum/ClassApct*VoteA&plus;ClassB/ClassBpct*VoteB}=97.38%)  


### 2.3 Cash-flow Example
#### 2.3.1 *34115* *CLAIRES STORES INC* 2006-05-25
|SHAOUTA|SHAOUTB|VOTEA|VOTEB|CLASSANUM|CLASSAPCT|CLASSBNUM|CLASSBPCT|VOTEPCT|DIVA|DIVB|CASHPCT|
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
|94,045,702|4,884,557 |	1.00 | 10.00 |3,694,450|3.90 | 4,313,732 | 88.30 |  32.70|0.30|0.15|Not Given|  

  
The data of above is given by DEF-14A.  
Cash-flow rights A= (3,694,450\*0.30+4,313,732\*0.15)/(94,045,708\*0.30+4,884,557\*0.15) = 6.06%  
Cash-flow rights B= (3,694,450\*0.30+4,313,732\*0.15)/(3,694,450/3.90\*0.30+4,313,732/88.3\*0.15) = 6.02%  
Cash-flow rights C= (94,045,708\*3.90\*0.30+4,884,557\*88.30\*0.15)/(94,045,708\*0.30+4,884,557\*0.15) = 6.04%  
Votes = 3,694,450\*1 + 4,313,732\*10 = 46,831,770  
Total Votes A = (3,694,450/3.90+4,313,732/88.30)\*100 = 143,582,624  
Total Votes B = (94,045,072\*1+4,884,557\*10) = 142,891,272  
Voting rights A = Votes/Total Votes A = 32.62%  
Voting rights B = Votes/Total Votes B = 32.77%




