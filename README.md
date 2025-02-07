# Flex Analytics Engineering Exercise

For context, I've never used or toyed with a piece of JavaScript before, nor have I really ever published publicly to Github. \
Consider this project an example of my resourcefulness, to get this data exercise done as best as possible all by myself.

**Step 1: Simplifying the deliverable (concept) from the raw script.** \
It seems like the JavaScript looks similar to a list of values in Python. Having seen JSON strings before, I know that they are used to concatenate a lot of data into a single cell/row so that multiple columns for additional data are not necessary. I can take the entire code block and organize it into its sections so that it can ***show me*** its structure and I can then use that to diagram the entities.

**Step 2: Question 1** \
So I pasted the JavaScript into VSCode and right-clicked "Format Document" to make it more readable. "Office Equipment" and "Computers and Accessories" seemed to have a line break that threw off the data structure, so I fixed those two lines and clicked Format Document again. That gave me a cleaner structure to read + chart. My chart can be found at [this file in the repsitory](https://github.com/rizvi14/flexanalyticseng/blob/main/flexanalyticseng.drawio)

**Step 3: Question 2, Part 1** \
I only know how to run SQL queries and to validate using SQL on top of a DB. Additionally, for the sake of this exercise, the DB needs to be local so pointing to something like BigQuery would not work. So I looked up a way in Anthropic's Clause to transform the JSON into a set of tables that I could then use for validation.

financial_data.sql and validation-step1-sqlite.py were both written by Claude to help me get the JSON into SQL.

**Step 4: Question 2, Part 2**
Once I had the list of tables that need to be created into a .db file, I then needed to read those tables using pandas so that I could write SQL on top of the .db contents. My approach was to validate the sum of all the child values compared to its immediate upper-level parent.

[These SQL lines were all written by myself](https://github.com/rizvi14/flexanalyticseng/blob/main/validation-step2-rule.py#L8-L76), and I used Stackoverflow just to understand how to use sqlite3 and pandas to use SQL on the .db file.


**




