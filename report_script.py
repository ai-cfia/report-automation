import os
import shutil
import re

import pandas as pd
import tkinter as tk

from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
from datetime import date

"""
Keys in the template:
- product
- name
- date
- iteration_date
- milestone
- milestones_table
- iteration_table
- image
- text
"""

def find_all_keys(template_path: str) -> list:
    regex = re.compile(r"\{\{.*?\}\}")

    with open(template_path, 'r') as file:
        lines = file.readlines()

    return [
        regex.findall(line)[0].replace("{{", "").replace("}}", "")
        for line in lines
        if regex.findall(line) !=[]
    ]

def generate_markdown(template_path: str, output_name: str, directory: str, **kwargs):

    charts, markdown_table = prepare_file_for_report(directory)
    output_path = f"reports/{output_name}"

    kwargs.update(markdown_table)
    kwargs.update(charts)

    with open(template_path, 'r') as f:
        content = f.read()

    for key, value in kwargs.items():
        content = content.replace(f'{{{{{key}}}}}', value)

    if not os.path.exists("reports"):
        os.makedirs("reports")

    with open(output_path, 'w') as f:
        f.write(content)

def prepare_file_for_report(directory:str):

    def get_word_before_extension(file:str):
        file_name = file.split(".")[0]
        return file_name.split()[-1]

    files = os.listdir(directory)
    markdown_table = {}
    images = []

    tsv_files = [file for file in files if file.endswith('.tsv')]

    img_files = [file for file in files if file.endswith('.png')] #or file.endswith('.jpg') or file.endswith('.jpeg')]

    for image in img_files:
        images.append(f'![{image}]({directory}/{image})')

    charts = {"image": "\n".join(images)}

    for file in tsv_files:
        df = pd.read_csv(f'{directory}/{file}', sep='\t')
        df_sorted = df.sort_values(by="Status")

        table_name = get_word_before_extension(file) + "_table"

        table = df_sorted.to_markdown(index=False)
        table = table.replace("nan", "")

        markdown_table[table_name.lower()] = table


    return (charts, markdown_table)


def start_programm():
    def find_widgets(frame, widget=tk.Entry):
            widgets = []

            child_frame = frame.winfo_children()

            for child in child_frame:
                if isinstance(child, widget):
                    widgets.append(child)
                widgets.extend(find_widgets(child, widget))

            return widgets

    def add_file():
        filename = filedialog.askopenfilename(initialdir = "/Downloads",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.tsv*"),
                                                       ("all files",
                                                        "*.*")))
        print(filename)

        destination_folder = "file_for_report"

        try:
            shutil.move(filename, destination_folder)

        except shutil.Error:
            messagebox.showerror("Error", "The file has already been added!")

        files = os.listdir("file_for_report")

        list_box = find_widgets(top_frame, widget=tk.Listbox)[0]
        list_box.delete(0, tk.END)

        for file in files:
            list_box.insert(tk.END, file)

    def remove_file():

        list_box = find_widgets(top_frame, widget=tk.Listbox)[0]
        selected_file = list_box.get(list_box.curselection())
        list_box.delete(list_box.curselection())

        os.remove("file_for_report/" + selected_file)

    def generate_report():
        entries = find_widgets(top_frame)

        child_frame = bottom_frame.winfo_children()
        text = child_frame[0]

        keys = {e.winfo_name(): e.get() for e in entries}
        keys.update({
            "date": date.today().strftime("%Y-%m-%d"),
            "text": text.get("1.0", tk.END)
        })

        generate_markdown("REPORT_TEMPLATE.md", f"{keys['date']}_report.md", "file_for_report", **keys)

        messagebox.showinfo("Report Generate", "The report has been generated successfully!")

    def create_info_frame():

        info_frame = tk.Frame(top_frame)
        info_frame.pack(expand=True, side=tk.LEFT, fill=tk.BOTH, padx=10)

        lbl_frame = tk.Frame(info_frame)
        lbl_frame.pack(side=tk.LEFT)

        ent_frame = tk.Frame(info_frame)
        ent_frame.pack(side=tk.LEFT)

        lbl_product = tk.Label(lbl_frame, text="Product Name: ")
        lbl_product.pack(side=tk.TOP, pady=5)
        lbl_author = tk.Label(lbl_frame, text="Author: ")
        lbl_author.pack(side=tk.TOP, pady=5)
        lbl_iteration = tk.Label(lbl_frame, text="Iteration Date: ")
        lbl_iteration.pack(side=tk.TOP, pady=5)
        lbl_milestone = tk.Label(lbl_frame, text="Milestone: ")
        lbl_milestone.pack(side=tk.TOP, pady=5)

        ent_product = tk.Entry(ent_frame, name="product")
        ent_product.pack(side=tk.TOP, pady=5)
        ent_author = tk.Entry(ent_frame, name="name")
        ent_author.pack(side=tk.TOP, pady=5)
        ent_iteration = tk.Entry(ent_frame, name="iteration_date")
        ent_iteration.pack(side=tk.TOP, pady=5)
        ent_milestone = tk.Entry(ent_frame, name="milestone")
        ent_milestone.pack(side=tk.TOP, pady=5)

    def create_file_entry_frame(directory):
        file_frame = tk.Frame(top_frame)
        file_frame.pack(expand=True, side=tk.LEFT, fill=tk.BOTH, padx=10)

        list_box = tk.Listbox(file_frame)
        list_box.pack(side=tk.TOP, expand=True, fill=tk.BOTH)


        if not os.path.exists(directory):
            os.makedirs(directory)

        files = os.listdir(directory)

        for file in files:
            list_box.insert(tk.END, file)

        btn_add = tk.Button(file_frame, text="Add file", command=add_file)
        btn_add.pack(side=tk.TOP)
        btn_remove = tk.Button(file_frame, text="Remove file", command=remove_file)
        btn_remove.pack(side=tk.TOP)

    def create_summary_report_frame():
        text_box = tk.Text(bottom_frame)
        text_box.pack(expand=True, side=tk.TOP)

        btn_generate = tk.Button(bottom_frame, text="Generate Report", command=generate_report)
        btn_generate.pack(side=tk.TOP)

    root = tk.Tk()
    root.title("Report Generator")
    root.geometry("800x720")

    ico = Image.open("img/logo.png")
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)

    lbl_tile = tk.Label(root, text="Report Generator", font=("Arial", 20))
    lbl_tile.pack(side=tk.TOP, pady=10)
    top_frame = tk.Frame(root)
    top_frame.pack(expand=True, side=tk.TOP, fill=tk.BOTH)
    bottom_frame = tk.Frame(root)
    bottom_frame.pack(expand=True, side=tk.TOP, fill=tk.BOTH, pady=10)

    create_file_entry_frame("file_for_report")
    create_info_frame()
    create_summary_report_frame()

    root.mainloop()

def main():
    start_programm()


if __name__ == "__main__":
    main()