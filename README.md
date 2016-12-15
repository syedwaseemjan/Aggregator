# Aggregator
Python application demonstrating how we can avoid re-inventing the wheel and save a lot of time by using third party libs. Few days back I was assigned some Big Data task at my former company. I spent a lot of energy and hours, completed the task but the results were "Horrible".

Here is somewhat matching summary of what was required of me.


You have an input file trades.dat containing json objects on each line.

{"tid": "40016498", "timestamp": "1404680438", "amount": "0.011", "type": "bid", "price": "630.99"}

Each row represents a time of transaction. You are supposed to aggregate the input by hours so if the timestamp for a row is 6:30PM, it should be place in 6PM group. For each group you are supposed to print the following items to stdout.

1- Time
2- Min, Max, First, Last value for price.
3- Sum of amount. 

At first I did this by manually iterating through the input, creating dictionaries, iterating again and calulating all the required items. The program performed horibbly as in some cases the input exceeded 5GB of dataset.


How to avoid this? Pandas and Numpy to the rescue.

#### 1. Clone the repository:

    $ git clone git@github.com:syedwaseemjan/Aggregator.git
    $ cd Aggregator

#### 2. Create and initialize virtualenv for the project:
    
    $ mkdir aggregator_env
    $ virtualenv aggregator_env
    $ source aggregator_env/bin/activate
    $ pip install -r requirements.py

#### 3. Run the script:
    
    $ python  aggregate.py trades.dat


