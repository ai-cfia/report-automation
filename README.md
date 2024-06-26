# report-automation :computer:

## Overview :rocket:

This repository contains the script to semi-automate biweekly reports for CFIA
AI-product and operation.

To see the current active products you can look at our project boards:

- [CFIA Project Board](https://github.com/orgs/ai-cfia/projects)

## Prerequisites :clipboard:

Currently, the script uses `tkinter` as its GUI library. Therefore, to use the
script you will need to have Python installed locally on your computer.

**Codespaces** users will have trouble running the application since
**Codespaces** and other cloud-based services don't have a display server.

## Usage :bookmark:

Run the script with the following command:

```bash
python report_script.py
```

You will see the following interface:

![Script Interface](https://github.com/ai-cfia/report-automation/assets/96267006/27872abb-560c-4e37-988f-6af89a63974f)

1. The right component allows you to add `.tsv` files. - Those files usually are
  the current iteration that is ending and the milestones you want to showcase.

   - You can collect those files from the project views. (Example Current
  Iteration)
   - ![get tsv example](img/import-tsv.gif)

1. The left component lets you enter important information such as `Product`,
   `Author` (your name), `Iteration Date` (see image below for example), and the
   `Milestones` you are working on.
   - ![image](https://github.com/ai-cfia/report-automation/assets/96267006/6b89baad-6c6c-4c3b-b944-ac4f889ea17c)
1. Finally the last component is the text entry where you can summarize the work
   that you have done for this iteration. It supports markdown.
1. When you finish writing your report click on the `Generate Report` button and
   it will generate a markdown report for you based on the `REPORT_TEMPLATE.md`.
   The report will be saved under `reports` folder.

### Specificity

- If your project doesn't have **Milestone**, just leave the field empty, and
  the report won't generate a section for **Milestone**.
- The `reports` folder is not push on the GitHub repository, but will be created
  the first time you use the script.

## Contribution :pencil2:

To contribute to this repository follow our [Contributing
Guide](https://github.com/ai-cfia/.github/blob/main/profile/CONTRIBUTING.md)
rules and norms.

## Possible Improvement :paperclip:

This script was done to help developer quickly write their biweekly report and
provide management with useful tables and information to keep track of the
project.

However, there is still some improvement that can be done. Here are some ideas
to potentially improve the script and provide more helpful tools to CFIA
developers:

- Use `flask` or other tools to create a web application that would allow the
  script to be deployed and used without the need to upload the current
  repository.

- Automated the summary with AI assistance by connecting
  [Assist](https://assist.inspection.alpha.canada.ca/)

And I'm sure there is plenty more improvement that can be done.
