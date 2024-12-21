import os
from PIL import Image
import pytesseract
import openpyxl

# Replace with Tesseract executable path if not in system PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(image_path):
  """Uses Tesseract OCR to extract text from an image."""
  img = Image.open(image_path)
  text = pytesseract.image_to_string(img)
  return text.strip()

def process_screenshot(image_path):
  """Extracts potential names and numbers from a WhatsApp screenshot."""
  text = extract_text(image_path)
  lines = text.splitlines()
  contacts = []
  for line in lines:
    # Basic pattern matching for name and number (can be improved based on UI elements)
    if ":" in line:
      parts = line.split(":")
      name = parts[0].strip()
      number = parts[1].strip()
      contacts.append({"name": name, "number": number})
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
  """Main function to process screenshots from a folder."""
  folder_name = input("Enter folder name containing screenshots: ")
  output_file = "extracted_contacts.xlsx"
  all_contacts = []
  for filename in os.listdir(folder_name):
    if filename.endswith(".png") or filename.endswith(".jpg"):
      image_path = os.path.join(folder_name, filename)
      contacts = process_screenshot(image_path)
      all_contacts.extend(contacts)
  generate_excel(all_contacts, output_file)
  print(f"Extracted contacts saved to {output_file}")

if __name__ == "__main__":
  main()
