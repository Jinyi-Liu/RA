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

### 63814
Don't know the way to deal with the dividend of common stock and preferred stock.
The Company has not declared any dividends on its capital stock.

### 64472
Common stock and Class B stock.  
No dividend data.  
Same voting right one any matter to be presented at the Annual Meeting. 
The holders of Common Stock and Class B Stock will vote separately as a class on the election of Directors. 

### 74046
More years than in the raw excel.

### 75208
Hold less than 0.1% of the outstanding shares.

### 78966
Common Stock; Series Three Preferred Stock.  
No cash dividends on common stock have been paid during any year.

### 83490
Common Stock and Series A Preferred Stock.  
No cash dividends were declared or paid by the Company during 2004 or 2003, and the Company does not intend to 
pay dividends on its Common Stock or Series A Preferred Stock in the foreseeable 

### 88948
5 types of voting stocks. 

### 89261
Class A stock and Class B stock have same voting power.  
EXX has not declared nor paid any dividends during the last two fiscal years. EXX does not 
intend to pay any cash dividends in the foreseeable future.

### 92103
The holders of the Edison International Common Stock have the right to cast a total of 325,796,087 votes. 
The holders of the SCE Cumulative Preferred Stock have the right to cast a total of 30,901,188 votes and the 
holder of the SCE Common Stock, Edison International, has the right to cast a total of 434,888,104 votes. 
Voting together as a class, the SCE shareholders have the right to cast a total of 465,789,292 votes.

### 94344
More years than in the raw excel and Class B Stock may not be paid any dividends.  
The certificate of incorporation provides that no cash dividends may be paid on its Class B Common Stock. 

### 96338
Ignore 1,010 shares of Class A Preferred Stock which entitled to a total of 505 votes.

### 96831
The current directors and current executive officers as a group held less than 1% of both types of shares.

### 97052
4 types of voting stocks.  
The Company historically has not paid cash dividends on its common stock.  The Company intends to retain all of its 
earnings for the future operation and growth of its business and does not intend to pay cash dividends in the foreseeable future.  
Additionally, certain covenants in our financing agreements restrict the payment of cash dividends.

### 99106
No data of the dividend of the Series A Convertible Preferred Stock in the 10-K file.

### 100493
Interesting. Sudden change of insider holdings of Class B Stock in 2011.

### 101538
 (1) 65,933,564 shares of common stock, (2) 177,904 shares of  Series C preferred stock, and 
 (3) 1,751, 005 shares of Series D preferred stock. The Company's Series B preferred stock does not have voting rights.   
We have not declared or paid any dividends to our stockholders during the last five years and do not anticipate paying dividends 
on our common stock in the foreseeable future.  Instead, we expect to retain earnings for the operation and expansion of our business.
Can not determined the cash-flow rights.

### 101830
Incorporation issue about the voting stocks (FON Stock and PCS Stock) which I can't determined.
 
 
 
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




