\# Lantern – Usage \& Implementation Documentation



\## 1. Project Overview



Lantern is a command-line task management application designed to help users organize and track their daily tasks.



This document explains the initial application commands and documents the data persistence functionality.



\## 2. Application Usage



\### 2.1 Add a Task



To create a new task, use the `add` command followed by the task title.



```bash

lantern add "Study Python"

```



This command creates a new task with the specified title.



\### 2.2 List Tasks



To display all existing tasks, use the `list` command.



```bash

lantern list

```



This command displays the tasks currently stored in Lantern.



\## 3. Data Persistence 



The data persistence functionality is implemented in `storage.py`.



Its purpose is to ensure that tasks are preserved between application executions using a local JSON file.



\### 3.1 Storage Location



Tasks are stored in:



```text

data/tasks.json

```



The storage module automatically creates the `data` directory if it does not already exist.



\### 3.2 Saving Tasks



The `save\_tasks()` function:



\- Accepts a list of task dictionaries.

\- Serializes the tasks into JSON using Python's `json` module.

\- Writes the data to `data/tasks.json`.

\- Uses UTF-8 encoding to support different languages.

\- Handles storage and serialization errors.



\### 3.3 Loading Tasks



The `load\_tasks()` function:



\- Checks whether the storage file exists.

\- Returns an empty list if no saved file exists.

\- Reads and deserializes the JSON data into Python objects.

\- Handles file-reading and invalid JSON errors.



\### 3.4 Data Persistence Testing



The storage module was tested by:



\- Saving a list containing multiple tasks.

\- Loading the saved tasks.

\- Comparing the loaded data with the original data.

\- Testing empty task lists.

\- Testing missing storage files.

\- Testing Arabic text serialization.



The save-and-load test confirmed that the retrieved data matched the original data, demonstrating successful data persistence.



\## 4. Implementation Responsibilities



\*\*Student B – Data Persistence and Documentation\*\*



The assigned responsibilities include:



\- Implementing `storage.py` for JSON-based data persistence.

\- Managing the storage file path using `pathlib`.

\- Handling file operations and relevant exceptions.

\- Testing saving and loading functionality.

\- Preparing this usage and implementation documentation.

