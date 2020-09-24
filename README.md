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

## 2. Process Method
### 2.1 Description


### 2.2 Voting Example
#### 2.2.1 1611988 Fifth Street Asset Management Inc. 2015-04-23
SHAOUTA: 6,000,033  
SHAOUTB: 42,856,854  
VOTEA: 1  
VOTEB: 5  
Class A num: 184,283 pct: 3.1%  
Class B num: 42,856,854,100 pct: 100.0%  
Votepct = 97.35% (Given by DEF-14A)  
The method using now
: ![equ](https://latex.codecogs.com/gif.latex?\frac{ClassAnum*VoteA&plus;ClassBnum*VoteB}{ClassAnum/ClassApct*VoteA&plus;ClassB/ClassBpct*VoteB}=97.38%)  


### 2.3 Cash-flow Example
##### 2.3.1 34115 CLAIRES STORES INC 2006-05-25
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




