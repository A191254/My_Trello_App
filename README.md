# Django Assignment 3: Trello App

You will be creating your first complete todo application using Django views, templates, models and forms.

## Initial Setup
- Make sure you have python and django installed.
- The project `todo_project` and app `trello_app` have already been created for you in this repository.
- IMPORTANT: Run the migrations already provided:
  - `python manage.py makemigrations`
  - `python manage.py migrate`
- To run the server use: `python manage.py runserver`.
- After server starts, you can visit `http://localhost:8000/` to see the changes.
- NOTE: PLEASE DO NOT REMOVE ANY LINE OF CODE ALREADY PROVIDED BY US, OTHERWISE TEST CASES MIGHT FAIL.

## Part 1: Create Board Model

- In `trello_app/models.py`, complete the `Board` class.
- In `TaskList` model, add `board` field which is foreign key to `Board` model.

## Part 2: Create Board Form

- In `trello_app/forms.py`, complete the `BoardForm` class which uses Django's `ModelForm`.
- In `TaskListForm` add the `board` field.

## Part 3: Complete the View to create Board

- In `trello_app/views.py`, complete the `add_board` method to add a board.

# NOTE
- Please read the comments and codes in the files to better understand the project structure.
- A lot of code has already been given to you, you need to finish the above 3 tasks.
- Search for TODO keyword in the above mentioned files to clearly find what needs to be done.