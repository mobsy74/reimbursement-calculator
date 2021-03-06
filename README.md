# Reimbursement Calculator exercise for Simple Thread
This is a simple program to calculate the required reimbursement for employee projects.

#### **Instructions:**

You have a set of projects, and you need to calculate a reimbursement amount for the set. Each project has a start date and an end date. The first day of a project and the last day of a project are always "travel" days. Days in the middle of a project are "full" days. There are also two types of cities a project can be in, high cost cities and low cost cities.

**A few rules:**

* First day and last day of a project, or sequence of projects, is a travel day.
* Any day in the middle of a project, or sequence of projects, is considered a full day.
* If there is a gap between projects, then the days on either side of that gap are travel days.
* If two projects push up against each other, or overlap, then those days are full days as well.
* Any given day is only ever counted once, even if two projects are on the same day.
* A travel day is reimbursed at a rate of 45 dollars per day in a low cost city.
* A travel day is reimbursed at a rate of 55 dollars per day in a high cost city.
* A full day is reimbursed at a rate of 75 dollars per day in a low cost city.
* A full day is reimbursed at a rate of 85 dollars per day in a high cost city.

#### **Running the program:**

* In a terminal window, clone the git repo.
* Navigate into the _reimbursement-calculator_ directory.
* Assuming you have a Python 3 environment installed and activated, type:

        python ReimbursementCalculator.py

* Follow the prompts to enter the required information for each project to be calculated.
* When all data is entered, the program will calculate each day's reimbursement cost, as well as the overall reimbursement amount for the project set.

* To run test scenarios:
 
        python ReimbursementCalculator.py test
