# RA
Dual-class stocks data processing.
## 1. Questions 
### 1.1 Option
Call option holders are not entitled to regular quarterly dividends. So when I compute the cash-flow rights with the 
numbers from DEF-14A "Security Ownershio of Certain Beneficial Owners and Management" shall I 
subtract those shares of common stock which may be acquired upon the exercise of options that are exercisable?

## 2. Companies not determined yet
### 28917 D
Class A Common Stock are empowered as a class to elect one-third of the Directors and the holders of Class B Common Stock are empowered as a class to elect two-thirds of the Directors.


### 30419
Common stock & Preferred stock(42.15 votes per share)  
No dividend paid for common stock.

### 

## 2. Process Method
### 2.1 Description


### 2.2 Example
#### 2.2.1 1611988 Fifth Street Asset Management Inc. 2015-04-23
SHAOUTA: 6,000,033  
SHAOUTB: 42,856,854  
VOTEA: 1  
VOTEB: 5  
Class A num: 184,283 pct: 3.1%  
Class B num: 42,856,854,100 pct: 100.0%  
Votepct = 97.35% (Given by DEF-14A)
Manual computed voting power = $\frac{ClassAnum\*VoteA+ClassBnum\*VoteB}{ClassAnum/ClassApct\*VoteA+ClassB/ClassBpct\*VoteB}$=97.38%