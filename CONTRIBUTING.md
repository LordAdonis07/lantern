\# Contributing to Lantern



Thank you for contributing to Lantern!



This document describes the conventions that all team members should follow when contributing to the project.



\## 1. Branch Naming



Create a separate branch for every task. Use descriptive names with the following prefixes:



\- `feature/` for new features.

\- `fix/` for bug fixes.

\- `docs/` for documentation changes.

\- `test/` for testing-related changes.



Examples:

\- `feature/list-sort`

\- `fix/empty-list-message`

\- `docs/usage-guide`



\## 2. Commit Message Convention



Use the following format:



`type: short description`



Accepted types:



\- `feat`: New functionality.

\- `fix`: Bug fixes.

\- `docs`: Documentation changes.

\- `test`: Adding or updating tests.

\- `chore`: Maintenance and configuration changes.



Examples:

\- `feat: add list sort option`

\- `fix: handle empty task list`

\- `docs: update usage guide`



\## 3. Pull Request Guidelines



Before submitting a pull request:



1\. Push your feature branch to GitHub.

2\. Ensure your changes are tested.

3\. Use a clear title following the commit message convention.

4\. Explain what changed and why in the description.

5\. Include the relevant issue reference using `Closes #N` when appropriate.

6\. Request a review from the other team member.



At least one approval is required before merging.



Resolve all review conversations before merging.



\## 4. Code Style



\- Use meaningful variable and function names.

\- Follow standard Python conventions (PEP 8).

\- Use clear indentation and formatting.

\- Keep functions focused on a single responsibility.

\- Add comments or docstrings when they improve clarity.



\## 5. Testing



Before submitting changes:



\- Run the application and verify the affected functionality.

\- Test normal and edge cases.

\- Check that existing functionality still works.

\- Run Python syntax checks where appropriate:



`python -m py\_compile lantern.py storage.py`



\## 6. Team Collaboration



\- Communicate with the other team member before modifying shared functionality.

\- Review the other member's pull requests.

\- Avoid committing generated files, temporary files, or local data.

\- Keep your branch synchronized with the latest project changes.

