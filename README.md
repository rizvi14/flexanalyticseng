# Flex Analytics Engineering Exercise

For context, I've never used or toyed with a piece of JavaScript before, nor have I really ever published publicly to Github.
Consider this project an example of my resourcefulness, to get this data exercise done as best as possible all by myself.

**Step 1: Simplifying the deliverable (concept) from the raw script.** \
It seems like the JavaScript looks similar to a list of values in Python. Having seen JSON strings before, I know that they are used to concatenate a lot of data into a single cell/row so that multiple columns for additional data are not necessary.

I can take the entire code block and organize it into its sections so that it can ***show me*** its structure and I can then use that to diagram the entities.

**Step 2: Question 1** \
So I pasted the JavaScript into VSCode and right-clicked "Format Document" to make it more readable. "Office Equipment" and "Computers and Accessories" seemed to have a line break that threw off the data structure, so I fixed those two lines and clicked Format Document again. That gave me a cleaner structure to read + chart. My chart can be found at [this file in the repsitory](https://github.com/rizvi14/flexanalyticseng/blob/main/flexanalyticseng.drawio)

**Step 3: Question 2, Part 1** \
I only know how to run SQL queries and to validate using SQL on top of a DB. Additionally, for the sake of this exercise, the DB needs to be local so pointing to something like BigQuery would not work. So I looked up a way in Anthropic's Clause to transform the JSON into a set of tables that I could then use for validation.

financial_data.sql and validation-step1-sqlite.py were both written by Claude to help me get the JSON into SQL.

**Step 4: Question 2, Part 2**
Once I had the list of tables that need to be created into a .db file, I then needed to read those tables using pandas so that I could write SQL on top of the .db contents. My approach was to validate the sum of all the child values compared to its immediate upper-level parent.

[These SQL lines were all written by myself](https://github.com/rizvi14/flexanalyticseng/blob/main/validation-step2-rule.py#L8-L76), and I used Stackoverflow just to understand how to use sqlite3 and pandas to use SQL on the .db file.


**Final Responses**
1. In order to view my chart, you can view it at its [public URL here](https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=flexanalyticseng.drawio#Uhttps%3A%2F%2Fraw.githubusercontent.com%2Frizvi14%2Fflexanalyticseng%2Fmain%2Fflexanalyticseng.drawio).
2. To run the validation script, clone my repository and run validation-step2-rule.py to see the results of validation that show results that look like the below. You may need to install the necessary python libraries to run the task.
   ![image](https://github.com/user-attachments/assets/3e568882-6c43-4c94-a2e3-9999327418f0)

Assumptions that I made include:
1. That the help from Claude properly inserted values correctly into the DB and interpreted the nesting structure correctly
2. That all numerical values have been formatted properly in the original JSON

Issues/inconsistencies:
1. ASSETS is capitalized while the other two accounting category items are not
2. In my validation at the ***category_level***, my SQL script is throwing an "Unbalanced" error even though the sum of Asset's children = to the ***lower_level_sum***. I can't tell if it's due to the column's format or something.
3. At the ***category_level*** Equity does not seem to be SUM-ing across Retained Earnings + Balance Adjustments, which tells me there's a data structure issue.
4. At first glance, it looked like Account ID is always NULL if that object has children, but Retained Earnings and Balance Adjustments are an exception to the rule and I can't understand why.
5. Accounts Payable being repeated as a parent/subparent twice is confusing.

*If I had more time next time:*
With my limitation only knowing SQL, this is a pretty inefficient way to do things. There are two unnecessary steps here: 1) Having to write the contents into a series of SQL CREATE TABLE statements and 2) Having to publish the CREATE TABLE statements into a .db file prior to running validaiton.

If I had the luxury of more time, I would have just learned Python in order to create a validation that takes the JSON pattern and splits it into the respective parent + immediate children and compares the sum of children to its immediate parent value.

**




