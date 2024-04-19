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

![Script Interface]() <!--Insert image here-->

1. The right component allows you to add `.tsv` files. - Those files usually are
  the current iteration that is ending and the milestones you want to showcase.
   - You can collect those files from the project views. (Example Current
  Iteration)
1. The left component lets you enter important information such as `Author`
   (your name), `Iteration Date`, and the `Milestones` you are working on.
1. Finally the last component is the text entry where you can summarize the work
   that you have done for this iteration. It supports markdown.
1. When you finish writing your report click on the `Generate Report` button and
   it will generate a markdown report for you based on the `REPORT_TEMPLATE.md`.

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
