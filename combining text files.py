import os

def combine_text_files(folder_path):
  """
  Combines all text files in a folder into a single output file named "ss.txt".

  Args:
      folder_path: The path to the folder containing the text files.
  """
  with open("ss.txt", "w") as outfile:
    for filename in os.listdir(folder_path):
      if filename.endswith(".txt"):
        filepath = os.path.join(folder_path, filename)
        with open(filepath, "r") as infile:
          outfile.write(infile.read())
          # Add a newline character between files (optional)
          outfile.write("\n")

# Example usage: Replace "your_folder_path" with the actual path to your folder
combine_text_files("E:\Contacts Extracting\compressed")
