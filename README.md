# Test Assignment

## Introduction

Hey! I hope you are doing well!

We have a short assignment for which we expect you to work for a day at max. At Armis, we try to apply good coding
practices, cover edge cases with unit and integration tests, and provide an environment where everyone can discuss any
technical aspect with data and challenge any decision. So, this test aims to see what your perspective
is for solving problems, clean coding, and testing :)

There are 3 different parts where you can find various questions. In each part, there are some simple tasks for fixing 
and refactoring to demonstrate your tech skills! Before starting to have a look at the questions, we would like to 
mention that there are no pre-defined answers to the questions. **We will be evaluating how you approach the problems 
rather than the answers.** So, we are open to all your ideas except the over-engineering ones! :)

You can create a new branch from the main branch. Then, you can make one commit for each part to review your work
easily.
After you finalize your assignment, you should push the commits to your feature, open a PR, then add GitHub user
names `aclet-armis` and `ktoprakucar` as reviewers. When you are done with all, you can ping us in case of any delay! :)

If you have any questions about anything, please do not hesitate to contact us!

## Requirements

- Before checking the code, you can install the requirements by the `pip install -r requirements.txt` command.
- To run the webservice for the 3rd question, you can run the `main` block in `src/bootstrap/main` to access the swagger
  page to test the webapp.

## Parts

Before the explanation, there are test classes for each part except the last one.

### 1. TextProcessService:

- There is something wrong with the `extract_information` method. Can you please modify the method to make it better? (
  for unexpected errors, you can raise an exception instead of returning something)
- `test_should_extract_information` has a dummy validation as you see. Can you please improve it?
- After your changes, can you please add some scenarios to the `TextProcessServiceTest`?
- P.s.
    - `unique_alphabetic_characters`: the characters **A to Z** or **a to z** (a, x, W, f, B, ...)
    - `unique_numerical_characters`: the positive numbers **0 to 9** (1, 342, 213, 04, 32, ...)
    - `unique_other_characters`: the characters **except numbers and the alphabetical characters** (-, !, ?, ... )

### 2. DataframeProcessService

- If you run the test in the `DataframeProcessServiceTest` class, you see it works a bit slowly. How can you improve it?
- After you fix it, can you please add another test with a sample dataframe that contains only _10_ text with better
  validations?

### 3. CustomerService:

There is a basic webservice to register customers. It registers the customer by **name**, **surname**, **age**, and *
*mail address** and return **the number of customers** from `in_memory`
database.

- In the method `register_customer` at the `src.application.customer_api.CustomerAPI` class, what is improper for you?
- In the method `register_customer` at `src.service.customer_service.CustomerService`,
    - Something works incorrectly. Can you please fix it?
    - It seems that the method needs some refactoring as well. Can you please do it?
    - **(bonus)** can you please implement an integration test for CustomerAPI?




