import openpyxl
import os

def parse_text(text_file):
  """Parses text from a file to extract contacts."""
  contacts = []
  try:
    with open(text_file, 'r') as f:
      lines = f.readlines()
      for line in lines:
        '''if line.startswith("~") and line.strip() != "~":
          name = line.strip()[1:]  # Remove leading tilde'''
        if line.startswith("+"):
          number = line.strip()
          name = "24 Phy "+str(number)
          if name:
            contacts.append({"name": name, "number": number})
            name = None  # Reset name for next contact
  except FileNotFoundError:
    print(f"Error: File '{text_file}' not found.")
  return contacts

def generate_excel(contacts, output_file):
  """Creates an Excel sheet with extracted contacts."""
  wb = openpyxl.Workbook()
  sheet = wb.active
  sheet.append(["Name", "Number"])
  for contact in contacts:
    sheet.append([contact["name"], contact["number"]])
  wb.save(output_file)

def main():
  """Main function to process text file and generate Excel sheet."""
  text_file = input("Enter text file name: ")
  output_file = "extracted_contacts.xlsx"
  contacts = parse_text(text_file)
  if contacts:  # Check if any contacts were extracted
    generate_excel(contacts, output_file)
    print(f"Extracted contacts saved to {output_file}")
  else:
    print("No contacts found in the text file.")

if __name__ == "__main__":
  main()


print("Hello")
